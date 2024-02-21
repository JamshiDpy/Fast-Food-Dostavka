import requests

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from handlers.users import global_file

cb = CallbackData("post", "action")


def categories(lang):
    category_list = requests.get("http://127.0.0.1:8000/bot/categories/").json()
    buttons_list = []
    for category in category_list:
        buttons_list.append(InlineKeyboardButton(text=category[f"name_{lang}"], callback_data=category['id']))
    # buttons_list.append(InlineKeyboardButton(text=global_file.BACK_BTN[lang], callback_data='back_to'))
    buttons_list.append(
        InlineKeyboardButton(text=global_file.HOME_PAGE_TEXT[lang], callback_data=cb.new(action="home_page"))
    )
    return InlineKeyboardMarkup(row_width=2).add(*buttons_list)


def products(products_list, lang):
    buttons_list = []
    for p in products_list:
        buttons_list.append(InlineKeyboardButton(text=p[f"name_{lang}"], callback_data=p['id']))

    buttons_list.append(
        InlineKeyboardButton(text=global_file.BACK_BTN[lang], callback_data=cb.new(action='back_to_category'))
    )
    buttons_list.append(
        InlineKeyboardButton(text=global_file.HOME_PAGE_TEXT[lang], callback_data=cb.new(action="home_page"))
    )
    return InlineKeyboardMarkup(row_width=2).add(*buttons_list)


def quantity(language, category):
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1️⃣", callback_data='1'),
             InlineKeyboardButton(text="2️⃣", callback_data='2'),
             InlineKeyboardButton(text="3️⃣", callback_data='3')],

            [InlineKeyboardButton(text="4️⃣", callback_data='4'),
             InlineKeyboardButton(text="5️⃣", callback_data='5'),
             InlineKeyboardButton(text="6️⃣", callback_data='6')],

            [InlineKeyboardButton(text="7️⃣", callback_data='7'),
             InlineKeyboardButton(text="8️⃣", callback_data='8'),
             InlineKeyboardButton(text="9️⃣", callback_data='9')],

            [InlineKeyboardButton(text=global_file.BACK_BTN[language], callback_data=f"back_to_products-{category}")],
            [InlineKeyboardButton(text="Bosh sahifa", callback_data=cb.new(action='home_page'))]

        ]

    )
    return btn


def new_order(order_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Qabul qildim", callback_data=f'i_accepted_{order_id}')]]
    )


def in_progress(order_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Tayyorlanmoqda...", callback_data=f'ready_{order_id}')]]
    )


new_order_out = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Qabul qildim", callback_data=cb.new(action='i_accepted_out'))]]
)

delivered = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Yetkazib berdim", callback_data=cb.new(action='delivered'))]]
)

none = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="...", callback_data='...')]]
)
