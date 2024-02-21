from aiogram.types import CallbackQuery
from aiogram.dispatcher.dispatcher import FSMContext

from loader import dp

from keyboards.inline.inline_keyboards import cb
from states.user_sates import Category, ProductState
from . import home_page, category


@dp.callback_query_handler(cb.filter(action=["home_page"]), state='*')
async def back_to_home_page(query: CallbackQuery, callback_data: dict, state: FSMContext):
    query.message.from_user['id'] = query.from_user.id
    await home_page.home(message=query.message)
    await query.message.delete()


@dp.callback_query_handler(cb.filter(action=['back_to_category', 'back_to_product']), state=ProductState.all_states)
async def back_to_category(query: CallbackQuery, callback_data: dict, state: FSMContext):
    query.message.from_user.id = query.from_user.id
    await category.categories(message=query.message, state=state)
    await query.message.delete()

