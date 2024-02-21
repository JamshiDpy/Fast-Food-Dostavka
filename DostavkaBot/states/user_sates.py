from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):
    request_phone_number = State()
    get_phone_number = State()
    vrf_code = State()


class HomePage(StatesGroup):
    home_page = State()


class Category(StatesGroup):
    categories = State()


class ProductState(StatesGroup):
    product = State()
    quantity = State()


class BasketStates(StatesGroup):
    finish = State()


class OrderStates(StatesGroup):
    start_order = State()
    shipping = State()
    go_get = State()

    location = State()

    new_order = State()

    time = State()


class SettingsStates(StatesGroup):
    settings = State()
    phone_number = State()
    vrf = State()
    vrf_back = State()
    language = State()


class Outside(StatesGroup):
    always = State()
