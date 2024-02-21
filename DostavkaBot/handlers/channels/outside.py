from aiogram.dispatcher import FSMContext
from geopy import Nominatim
import requests

from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from data.config import ChannelOutside
from loader import dp
from states.user_sates import Outside
from keyboards.inline import inline_keyboards

geolocator = Nominatim(user_agent="Dostavka_bot")


async def new_order(query: CallbackQuery, order_id):
    orders = requests.get(f"http://127.0.0.1:8000/bot/orders/{order_id}/").json()
    msg = f"Buyurtma:\nBuyutmachi: {orders['user']['phone_number']}\nTelegram: {orders['user']['telegram_username']}\n"
    for order in orders['orders']:
        msg += f"Nomi: {order['product']['name_uz']}\n"
        msg += f"Miqdori: {order['quantity']}\n\n"
    location = geolocator.reverse(f"{orders['latitude']}, {orders['longitude']}")
    msg += f"\n{location.address}"
    await query.bot.send_message(chat_id=ChannelOutside, text=msg, reply_markup=inline_keyboards.new_order_out)
    await query.bot.send_location(chat_id=ChannelOutside, latitude=orders['latitude'], longitude=orders['longitude'])


@dp.callback_query_handler(inline_keyboards.cb.filter(action=['i_accepted_out']))
async def i_accept(query: CallbackQuery) -> None:
    await query.bot.edit_message_reply_markup(
        chat_id=ChannelOutside, message_id=query.message.message_id, reply_markup=inline_keyboards.delivered
    )


@dp.callback_query_handler(*[inline_keyboards.cb.filter(action=['delivered'])])
async def delivered_successfully(query: CallbackQuery) -> None:
    await query.bot.edit_message_reply_markup(
        chat_id=ChannelOutside, message_id=query.message.message_id, reply_markup=inline_keyboards.none
    )
