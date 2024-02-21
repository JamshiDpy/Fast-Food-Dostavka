import random
import re
import requests
from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from states.user_sates import SettingsStates
from . import global_file as gb
from keyboards.default import keyboards
from . import home_page


@dp.message_handler(lambda message: message.text in [gb.BACK_BTN['uz'], gb.BACK_BTN['ru']],
                    state=SettingsStates.settings)
async def settings_back(message: Message):
    await home_page.home(message)


@dp.message_handler(state=SettingsStates.settings)
async def select_settings(message: Message, state: FSMContext):
    if message.text == gb.SETTINGS_BTN['uz'][1]:
        await message.answer('Yangi telefon raqaminggizni kiriting.\nNamuna: 901234567',
                             reply_markup=ReplyKeyboardMarkup(
                                 keyboard=[[KeyboardButton(gb.BACK_BTN['uz'])]], resize_keyboard=True
                             ))
        await SettingsStates.phone_number.set()
        await state.update_data({'lang': 'uz'})
    elif message.text == gb.SETTINGS_BTN['uz'][2]:
        await message.answer("Kerakli tilni tanlang.", reply_markup=keyboards.select_language())
        await SettingsStates.language.set()
        await state.update_data({'lang': 'uz'})
    elif message.text == gb.SETTINGS_BTN['ru'][1]:
        await message.answer("Введите новый номер телефона.\nОбразец: 901234567",
                             reply_markup=ReplyKeyboardMarkup(
                                 keyboard=[[KeyboardButton(gb.BACK_BTN['ru'])]], resize_keyboard=True
                             ))
        await SettingsStates.phone_number.set()
        await state.update_data({"lang": 'ru'})
    elif message.text == gb.SETTINGS_BTN['ru'][2]:
        await message.answer("Выберите желаемый язык.", reply_markup=keyboards.select_language())
        await SettingsStates.language.set()
        await state.update_data({"lang": 'ru'})


@dp.message_handler(lambda message: message.text in [gb.BACK_BTN['uz'], gb.BACK_BTN['ru']],
                    state=SettingsStates.phone_number)
async def settings_phone_back(message: Message):
    if message.text == gb.BACK_BTN['uz']:
        message.text = gb.HOME_PAGE_BUTTONS['uz'][6]
    else:
        message.text = gb.HOME_PAGE_BUTTONS['ru'][6]
    await home_page.settings(message)


@dp.message_handler(regexp=re.compile("^\d{2}\d{7}$"), state=SettingsStates.phone_number)
async def reset_phone_number(message: Message, state: FSMContext):
    vrf_code = random.randint(1000, 10000)
    print(vrf_code)
    await state.update_data(
        {'phone_number': f"+998{message.text}", "vrf_code": vrf_code}
    )
    data = await state.get_data()
    await message.answer(gb.PHONE_NUMBER_VERIFICATION[data['lang']])
    await SettingsStates.vrf.set()


@dp.message_handler(lambda message: message.text == "O'zbek 🇺🇿", state=SettingsStates.language)
@dp.message_handler(lambda message: message.text == "Русский 🇷🇺", state=SettingsStates.language)
async def reset_language(message: Message):
    if message.text == "O'zbek 🇺🇿":
        requests.put(f"http://127.0.0.1:8000/bot/users/{message.from_user.id}/", data={"language": 'uz'})
        await message.answer("Tilni o'zgartirish muvaffaqiyatli bajarildi.")
        await home_page.home(message)
    else:
        requests.put(f"http://127.0.0.1:8000/bot/users/{message.from_user.id}/", data={"language": 'ru'})
        await message.answer("Смена языка прошла успешно")
        await home_page.home(message)


@dp.message_handler(lambda message: message.text in [gb.BACK_BTN['uz'], gb.BACK_BTN['ru']], state=SettingsStates.vrf)
async def vrf_back(message: Message, state: FSMContext):
    if message.text == gb.BACK_BTN['uz']:
        message.text = gb.SETTINGS_BTN['uz'][1]
    else:
        message.text = gb.SETTINGS_BTN['ru'][1]
    await select_settings(message, state)


@dp.message_handler(state=SettingsStates.vrf)
async def vrf(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if message.text == str(data['vrf_code']):
        await message.answer(gb.SETTINGS_PHONE[data['lang']],
                             reply_markup=ReplyKeyboardMarkup(
                                 [[KeyboardButton(gb.BACK_BTN[data['lang']])]], resize_keyboard=True)
                             )
        requests.put(f'http://127.0.0.1:8000/bot/users/{message.from_user.id}',
                     data={'phone_number': data['phone_number']})
        await home_page.home(message)
        await state.finish()
    else:
        await message.answer(gb.VRF_CODE_ERROR_MESSAGE[data['lang']])
