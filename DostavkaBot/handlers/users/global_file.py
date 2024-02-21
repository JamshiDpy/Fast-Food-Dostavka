# Select_language = {'uz': "Tilni tanlang", 'ru': ""}
# PHONE NUMBER
REQUEST_PHONE = {
    "uz": "Telefon raqamingizni kiritng: <b>901234567</b>\n"
          "Agar telegraminggizga bog'langan raqaminggizdan foydalansangiz pastdagi tugmani bosing. 👇",
    "ru": "Введите свой номер телефона: <b>901234567</b>\n"
          "Если вы используете номер, привязанный к Telegram, нажмите кнопку ниже. 👇",
    "text": {
        "uz": "Telefon raqamni yuborish 📞", "ru": "Отправить номер телефона 📞"
    }

}
# END PHONE NUMBER
INVALID_FORMAT_PHONE_NUMBER = {
    'uz': "Telefon raqamni namunadagidek kiriting\n\n<b>901234567</b>",
    'ru': "Введите номер телефона как в примере\n\n<b>901234567</b>"
}

PHONE_NUMBER_VERIFICATION = {
    'uz': "Telefon raqamingizni tasdiqlash uchun sizga 4 xonali kod yubordik.",
    'ru': "Мы отправили вам 4-значный код для подтверждения вашего номера телефона."
}

VRF_CODE_ERROR_MESSAGE = {
    'uz': "Tasdiqlash kodi mos kelmadi.",
    'ru': "Код подтверждения не совпал."
}

# HOME PAGE
HOME_PAGE_TEXT = {'uz': "Bosh sahifa 🏠", 'ru': "Домашняя страница 🏠"}
# END HOME PAGE

# HOME PAGE
HOME_PAGE_BUTTONS = {
    'uz': {
        1: "Menyu 📕",
        2: "Savatcha 🛒",
        3: "Biz haqimizda 👨‍👩‍👧‍👦", 4: "Aloqa 📞",
        5: "Fikr va taklif ✍️", 6: "Sozlamalar ⚙️",
        7: "Bizning manzil 📍"
    },
    'ru': {
        1: "Меню 📕",
        2: "Корзина 🛒",
        3: "О нас 👨‍👩‍👧‍👦", 4: "контакт 📞",
        5: "Мысли и предложения ✍️", 6: "Настройки ⚙️",
        7: "Наш адрес 📍"
    }
}
# END HOME PAGE

# CATEGORIES

# END CATEGORIES

# PRODUCT
PRODUCT_NULL = {
    'uz': "Ushbu bo\'limda xozircha maxsulot yo\'q 🤷‍♂️", 'ru': "В этом разделе на данный момент нет товаров 🤷‍♂️"
}
# END PRODUCT

# BASKET
JOIN_BASKET = {
    'uz': {"name": "nomi:", "desc": "tafsilot:", "price": "narxi:", "qty": "Miqdorini tanlang, yoki yozing.",
           'sum': "Jami narxi:", "qty_basket": "miqdori:"},
    'ru': {"name": "имя:", "desc": "деталь:", "price": "цена:", "qty": "Выберите или введите сумму.",
           'sum': "Итоговая цена:", "qty_basket": "количество"}
}

JOIN_BASKET_MSG = {
    'uz': "Maxsulot savatchaga joylanda.\nAgar xoxlasangiz yana biror narsa qo'shing.",
    'ru': "Товар помещается в корзину.\nЕсли хотите, добавьте что-нибудь еще."
}

BASKET_EMPTY = {
    "uz": "Hozircha savatchangiz bo'sh", "ru": "Ваша корзина пуста"
}

CLEAR_BASKET = {'uz': 'Savatcha tozalandi 🛒', 'ru': 'Корзина очищена 🛒'}
BUY = {
    'uz': {'buy': 'Buyurtma qilish 📤', "delete": 'savatni tozalash ❌'},
    'ru': {"buy": "заказать 📤", "delete": "очистить корзину ❌"}
}
# EDN BASKET


# ORDER
ORDER_TYPE = {'uz': 'Buyurtma turini tanlang.', 'ru': 'Выберите тип заказа.'}
ORDER_TYPE_BUTTON = {
    'uz': {1: "Yetkazib berish 🛵", 2: "Borib olish 🚶"},
    'ru': {1: "Доставка 🛵", 2: "Забирайте 🚶"}
}
DELIVERY_TEXT = {'uz': "Yetkazib berish uchun joylashuvingizni yuboring. 📍", 'ru': "Укажите место доставки. 📍"}
GO_GET = {""}
LOCATION_BUTTON = {'uz': 'Joylashuvni yuborish 📍', 'ru': 'Отправить местоположение 📍'}

DISTANCE = {
    'uz': {'true': 'Buyurtmangiz qabul qilindi. Tez orada yetkazamiz. 😊', 'false': "Sizning manzilingiz yetkazib berish doirasidan uzoqda. 😔"},
    'ru': {"true": 'Ваш заказ принят. Мы доставим в ближайшее время. 😊', 'false': "Ваш адрес вне зоны доставки. 😔"}
}
TIME = {
    'uz': "Necha daqiqada kelishingizni yozing\nMisol uchun : 10",
    'ru':"Напишите через сколько минут вы приедете\n Например: 10"
}
# END ORDER


CHOOSE = {'uz': 'Tanlang:', 'ru': "Выбирать:"}

BACK_BTN = {
    'uz': "Ortga 🔙", 'ru': "Назад 🔙"
}


# SETTINGS
SETTINGS_MSG = {'uz': "Nimani o'zgartirmoqchisiz ?", 'ru': 'Что вы хотите изменить?'}
SETTINGS_BTN = {
    'uz': {1: "Telefon raqam", 2: 'Til'}, 'ru': {1: "Номер телефона", 2: "Язык"}
}
SETTINGS_PHONE = {'uz': "Telefon raqaminggiz muvaffaqiyatli yangilangi.", 'ru': "Ваш номер телефона успешно обновлен."}
# END SETTINGS