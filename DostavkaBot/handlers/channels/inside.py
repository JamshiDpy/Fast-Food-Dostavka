import requests

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.dispatcher import FSMContext

from data.config import ADMINS
from data.config import ChannelInside
from keyboards.inline import inline_keyboards
from keyboards.inline.inline_keyboards import cb
from states.user_sates import OrderStates

from loader import dp
from . import outside


async def new_order(message: Message, lat=None, long=None):
    if lat and long:
        order_list = requests.post(
            f"http://127.0.0.1:8000/bot/create-orders/{message.from_user.id}/{lat}/{long}/").json()
        msg = f"Buyurtma:\nBuyurtma raqami: {order_list['id']}\n"

        for order in order_list['orders']:
            msg += f"Nomi: {order['product']['name_uz']}\n"
            msg += f"Miqdori: {order['quantity']}\n\n"
        await message.bot.send_message(chat_id=ChannelInside, text=msg,
                                       reply_markup=inline_keyboards.new_order(order_list['id']))
    else:
        order_list = requests.post(f"http://127.0.0.1:8000/bot/create-orders/{message.from_user.id}").json()
        msg = f"Buyurtma:\nBuyurtma raqami: {order_list['id']}\n"

        for order in order_list['orders']:
            msg += f"Nomi: {order['product']['name_uz']}\n"
            msg += f"Miqdori: {order['quantity']}\n\n"

        msg += "<b>TEZ ORADA O'ZI KELADI.</b>"
        await message.bot.send_message(chat_id=ChannelInside, text=msg)


@dp.callback_query_handler(*[lambda query: query.data[:11] == "i_accepted_"])
async def in_progress(query: CallbackQuery):
    await query.bot.edit_message_reply_markup(
        ChannelInside, message_id=query.message.message_id,
        reply_markup=inline_keyboards.in_progress(query.data.split('_')[-1])
    )


@dp.callback_query_handler(*[lambda query: query.data.startswith('ready_')])
async def product_done(query: CallbackQuery):
    await query.message.delete()
    await outside.new_order(query, query.data.split('_')[-1])
