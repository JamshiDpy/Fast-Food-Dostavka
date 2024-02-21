from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from handlers.users import global_file


def select_language():
    return ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(*[
        KeyboardButton(text="O'zbek 🇺🇿"), KeyboardButton(text="Русский 🇷🇺")
    ])


# def select_language_2():
#     return ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(*[
#         KeyboardButton(text="O'zbek 🇺🇿"), KeyboardButton(text="Русский 🇷🇺"),
#     ])


def phone_number(text):
    return ReplyKeyboardMarkup([[KeyboardButton(text=text, request_contact=True)]], resize_keyboard=True)


def home_page(language):
    category = global_file.HOME_PAGE_BUTTONS[language]
    buttons = ReplyKeyboardMarkup(
        [
            [KeyboardButton(category[1])],
            [KeyboardButton(category[2])],
            [KeyboardButton(category[3]), KeyboardButton(category[4])],
            [KeyboardButton(category[5]), KeyboardButton(category[6])],
            [KeyboardButton(category[7])]
        ], resize_keyboard=True
    )
    return buttons


def buy(lang):
    return ReplyKeyboardMarkup(
        [[KeyboardButton(global_file.BUY[lang]['delete']), KeyboardButton(global_file.BUY[lang]['buy'])],
         [KeyboardButton(global_file.BACK_BTN[lang])]],
        resize_keyboard=True
    )


def order_type(lang):
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(global_file.ORDER_TYPE_BUTTON[lang][1]),
             KeyboardButton(global_file.ORDER_TYPE_BUTTON[lang][2])],
            [KeyboardButton(global_file.BACK_BTN[lang])]
        ], resize_keyboard=True
    )


def location(lang):
    return ReplyKeyboardMarkup([[KeyboardButton(global_file.LOCATION_BUTTON[lang], request_location=True)]],
                               resize_keyboard=True)


def settings(lang):
    buttons = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(global_file.SETTINGS_BTN[lang][1]), KeyboardButton(global_file.SETTINGS_BTN[lang][2])],
            [KeyboardButton(global_file.BACK_BTN[lang])]
        ], resize_keyboard=True
    )
    return buttons
