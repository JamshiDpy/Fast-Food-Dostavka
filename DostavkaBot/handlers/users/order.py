import requests
from aiogram.dispatcher import FSMContext
from geopy import distance

from aiogram.types import Message, ReplyKeyboardRemove, ContentType

from keyboards.default import keyboards
from states.user_sates import BasketStates, OrderStates

from loader import dp
from data.config import ChannelInside

from . import global_file as gb
from . import basket
from handlers.channels import inside
from handlers.channels import outside
from . import home_page


@dp.message_handler(lambda message: message.text in [gb.BUY['uz']['buy'], gb.BUY['ru']['buy']],
                    state=BasketStates.finish)
async def statr_buy(message: Message):
    if message.text == gb.BUY['uz']['buy']:
        await message.answer(text=gb.ORDER_TYPE['uz'], reply_markup=keyboards.order_type('uz'))
    else:
        await message.answer(text=gb.ORDER_TYPE['ru'], reply_markup=keyboards.order_type('ru'))
    await OrderStates.start_order.set()


@dp.message_handler(lambda message: message.text in [gb.BACK_BTN['uz'], gb.BACK_BTN['ru']],
                    state=OrderStates.start_order)
async def start_order_back_basket(message: Message) -> None:
    await basket.open_basket(message)


@dp.message_handler(lambda message: message.text in [gb.ORDER_TYPE_BUTTON['uz'][1], gb.ORDER_TYPE_BUTTON['ru'][1]],
                    state=OrderStates.start_order)
async def select_delivery(message: Message):
    if message.text == gb.ORDER_TYPE_BUTTON['uz'][1]:
        await message.answer(gb.DELIVERY_TEXT['uz'], reply_markup=keyboards.location('uz'))
    else:
        await message.answer(gb.DELIVERY_TEXT['ru'], reply_markup=keyboards.location('ru'))
    await OrderStates.location.set()


@dp.message_handler(lambda message: message.text in [gb.ORDER_TYPE_BUTTON['uz'][2], gb.ORDER_TYPE_BUTTON['ru'][2]])
async def select_delivery_2(message: Message):
    if message.text == gb.ORDER_TYPE_BUTTON['uz'][2]:
        await message.answer(text="Buyurtmangiz qabul qilindi, Kelguninggizcha tayyorlab qo'yamiz. 😊")
        await inside.new_order(message)
    elif message.text == gb.ORDER_TYPE_BUTTON['ru'][2]:
        await message.answer("Ваш заказ обработан и будет готов к прибытию. 😊")
        await inside.new_order(message)


# @dp.message_handler(state=OrderStates.time)
# async def time(message: Message):
#     try:
#         a = int(message.text)
#     except:


@dp.message_handler(content_types=ContentType.LOCATION, state=OrderStates.location)
async def check_location(message: Message, state: FSMContext):
    user = requests.get(f"http://127.0.0.1:8000/bot/users/{message.from_user.id}").json()
    location_from = (40.62621353367795, 72.5008179405125)
    location_to = (message.location.latitude, message.location.longitude)

    if distance.distance(location_from, location_to).km > 5:
        await message.answer(gb.DISTANCE[user['language']]['false'])
    else:
        await message.answer(gb.DISTANCE[user['language']]['true'])
        await inside.new_order(message, location_to[0], location_to[1])
        await home_page.home(message)
