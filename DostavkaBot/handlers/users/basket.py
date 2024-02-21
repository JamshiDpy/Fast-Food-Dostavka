import requests
from aiogram.types import Message

from . import global_file as gb
from keyboards.default import keyboards

from states.user_sates import BasketStates
from . import home_page

from loader import dp


async def open_basket(message: Message):
    basket = requests.get(f"http://127.0.0.1:8000/bot/basket/{message.from_user.id}").json()
    if basket:
        msg = '🛒\n'
        total_price = 0.0
        for b in basket:
            msg += f"""<b>{gb.JOIN_BASKET[b['user']['language']]['name']} {b['product'][f"name_{b['user']['language']}"]}</b>\n"""
            msg += f"""<b>{gb.JOIN_BASKET[b['user']['language']]['qty_basket']} {b['quantity']}</b>\n"""
            msg += f"""<b>{gb.JOIN_BASKET[b['user']['language']]['price']} {b['total_price']}</b>\n\n"""
            total_price += (int(b['quantity']) * float(b['product']['price']))

        msg += "<b>{} {:0,.0f} so'm</b>".format(gb.JOIN_BASKET[basket[0]['user']['language']]['sum'], total_price)

        await message.answer(text=msg, reply_markup=keyboards.buy(basket[0]['user']['language']))
        await BasketStates.finish.set()
    else:
        user = requests.get(f"http://127.0.0.1:8000/bot/users/{message.from_user.id}").json()
        await message.answer(gb.BASKET_EMPTY[user['language']])
        await home_page.home(message)


@dp.message_handler(lambda message: message.text in [gb.BUY['uz']['delete'], gb.BUY['ru']['delete']],
                    state=BasketStates.finish)
async def clear_basket(message: Message) -> None:
    basket = requests.delete(f"http://127.0.0.1:8000/bot/basket/{message.from_user.id}").json()

    await message.answer(gb.CLEAR_BASKET[basket['user_lang']])
    await home_page.home(message)


@dp.message_handler(lambda message: message.text in [gb.BACK_BTN['uz'], gb.BACK_BTN['ru']], state=BasketStates.finish)
async def basket_back_home(message: Message) -> None:
    await home_page.home(message)
