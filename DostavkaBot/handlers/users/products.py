import requests
import asyncio

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.dispatcher import FSMContext

from loader import dp

from states.user_sates import Category, ProductState
from keyboards.inline import inline_keyboards

from . import global_file as gb
from . import home_page
from . import category


@dp.callback_query_handler(state=Category.categories)
async def products(query: CallbackQuery, state: FSMContext):
    await query.answer()
    await query.message.delete()
    user = requests.get(f"http://127.0.0.1:8000/bot/users/{query.from_user.id}").json()
    products_list = requests.get(f"http://127.0.0.1:8000/bot/products/{query.data}").json()
    if products_list:
        await query.message.answer_photo(
            photo=requests.get(f"http://127.0.0.1:8000{products_list[-1]['category']['image']}").content,
            caption=products_list[-1]['category'][f"name_{user['language']}"],
            reply_markup=inline_keyboards.products(products_list, user['language'])
        )
        await ProductState.product.set()
    else:
        await query.message.answer(gb.PRODUCT_NULL[user['language']])
        await asyncio.sleep(1)
        query.message.from_user.id = query.from_user.id
        await category.categories(query.message, state)


@dp.callback_query_handler(state=ProductState.product)
async def get_product(query: CallbackQuery, state: FSMContext):
    await query.message.delete()
    user = requests.get(f"http://127.0.0.1:8000/bot/users/{query.from_user.id}").json()
    product = requests.get(f"http://127.0.0.1:8000/bot/product-detail/{query.data}").json()
    caption = "<b>{}\n{} {:0,.0f}\n{} {}</b>\n\n{}".format(
        product[f"name_{user['language']}"],
        gb.JOIN_BASKET[user['language']]['price'], product['price'],
        gb.JOIN_BASKET[user['language']]['desc'], product[f"description_{user['language']}"],
        gb.JOIN_BASKET[user['language']]['qty']
    )
    await query.message.answer_photo(
        photo=requests.get(f"http://127.0.0.1:8000{product['image']}").content,
        caption=caption,
        reply_markup=inline_keyboards.quantity(user['language'], product['category']['id'])
    )

    await state.update_data({"product": product['id']})
    await ProductState.quantity.set()


@dp.callback_query_handler(state=ProductState.quantity)
@dp.message_handler(state=ProductState.quantity)
async def select_quantity(query: CallbackQuery, state: FSMContext) -> None:
    if query.data.startswith('back_to_products'):
        query.data = query.data.split('-')[-1]
        await products(query, state)
    await query.message.delete()
    product = await state.get_data()
    basket = requests.post(
        url=f"http://127.0.0.1:8000/bot/add-basket/{query.from_user.id}/{product['product']}/{query.data}/"
    )
    await state.finish()
    if basket.status_code == 201:
        await query.answer(
            text=gb.JOIN_BASKET_MSG[basket.json()['user']['language']], show_alert=True
        )
        query.message.from_user.id = query.from_user.id
        await home_page.home(message=query.message)




