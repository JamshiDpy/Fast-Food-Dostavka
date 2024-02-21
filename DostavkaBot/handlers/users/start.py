import requests

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.dispatcher import FSMContext

from loader import dp

from . import home_page
from . import global_file
from . import registration

from keyboards.default import keyboards
from states.user_sates import Registration


# @dp.message_handler(CommandStart(), )

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    user = requests.get(f"http://127.0.0.1:8000/bot/users/{message.from_user.id}")
    if user.status_code == 200:
        await home_page.home(message)

    else:
        await message.answer(f"Salom, {message.from_user.full_name}!\nTilni tanlang\nВыберите язык",
                             reply_markup=keyboards.select_language())
        await Registration.request_phone_number.set()
    # await registration.request_phone_number(message=message, state=state)
