import requests

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.dispatcher import FSMContext

from loader import dp

from . import global_file

from states.user_sates import Category
from keyboards.inline import inline_keyboards


async def categories(message: Message, state: FSMContext):
    user = requests.get(f"http://127.0.0.1:8000/bot/users/{message.from_user.id}").json()
    ctg_image = requests.get("http://127.0.0.1:8000/bot/category-main-image/").json()
    await message.answer(global_file.CHOOSE[user['language']], reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo=requests.get(f"http://127.0.0.1:8000{ctg_image['image']}").content,
        reply_markup=inline_keyboards.categories(user['language'])
    )

    await Category.categories.set()
