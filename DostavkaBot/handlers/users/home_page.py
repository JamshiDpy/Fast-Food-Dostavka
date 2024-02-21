import re

import requests

from aiogram.types import Message
from aiogram.dispatcher.dispatcher import FSMContext

from keyboards.default import keyboards
from loader import dp

from states.user_sates import HomePage, SettingsStates

from . import global_file as gb
from . import category
from . import basket
from data.config import CAFE_LOCATION


async def home(message: Message):
    user = requests.get(f"http://127.0.0.1:8000/bot/users/{message.from_user.id}").json()
    await message.answer(
        gb.HOME_PAGE_TEXT[user['language']],
        reply_markup=keyboards.home_page(user['language'])
    )
    await HomePage.home_page.set()


@dp.message_handler(state=HomePage.home_page)
async def relation_func(message: Message, state: FSMContext):
    if message.text in [gb.HOME_PAGE_BUTTONS['uz'][1], gb.HOME_PAGE_BUTTONS['ru'][1]]:
        await category.categories(message, state)
    elif message.text in [gb.HOME_PAGE_BUTTONS['uz'][2], gb.HOME_PAGE_BUTTONS['ru'][2]]:
        await basket.open_basket(message)
    elif message.text in [gb.HOME_PAGE_BUTTONS['uz'][7], gb.HOME_PAGE_BUTTONS['ru'][7]]:
        await cafe_location(message)
    elif message.text in [gb.HOME_PAGE_BUTTONS['uz'][6], gb.HOME_PAGE_BUTTONS['ru'][6]]:
        await settings(message)


async def settings(message: Message) -> None:
    if message.text == gb.HOME_PAGE_BUTTONS['uz'][6]:
        await message.answer(gb.SETTINGS_MSG['uz'], reply_markup=keyboards.settings('uz'))
    else:
        await message.answer(gb.SETTINGS_MSG['ru'], reply_markup=keyboards.settings('ru'))

    await SettingsStates.settings.set()


async def cafe_location(message: Message):
    await message.answer_location(latitude=CAFE_LOCATION.split(',')[0], longitude=CAFE_LOCATION.split(',')[1])
