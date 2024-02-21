import random
import re
import requests

from aiogram.types import Message, ContentTypes
from aiogram.dispatcher.dispatcher import FSMContext

from loader import dp

from . import global_file
from data.config import SMS_TOKEN
from keyboards.default import keyboards
from states.user_sates import Registration

from . import home_page


@dp.message_handler(lambda message: message.text in ["O'zbek 🇺🇿", "Русский 🇷🇺"],
                    state=Registration.request_phone_number)
async def request_phone_number(message: Message, state: FSMContext):
    if message.text == "O'zbek 🇺🇿":
        await message.answer(global_file.REQUEST_PHONE['uz'],
                             reply_markup=keyboards.phone_number(global_file.REQUEST_PHONE['text']['uz']))
        await state.update_data({"language": "uz"})
    else:
        await message.answer(global_file.REQUEST_PHONE['ru'],
                             reply_markup=keyboards.phone_number(global_file['text']["ru"]))
        await state.update_data({"language": "ru"})
    await Registration.get_phone_number.set()


@dp.message_handler(content_types=ContentTypes.CONTACT, state=Registration.get_phone_number)
@dp.message_handler(state=Registration.get_phone_number, regexp=re.compile("^\d{2}\d{7}$"))
async def get_phone_number(message: Message, state: FSMContext):
    data = await state.get_data()

    if message.contact:
        await state.update_data({'phone_number': message.contact.phone_number})
        phone_number = message.contact.phone_number
    else:
        await state.update_data({"phone_number": f"+998{message.text}"})
        phone_number = '998' + message.text

    await message.answer(text=global_file.PHONE_NUMBER_VERIFICATION[data['language']])

    vrf_code = random.randint(1000, 10000)
    # SEND SMS
    url = "https://notify.eskiz.uz/api/message/sms/send"
    payload = {'mobile_phone': phone_number,
               'message': f'Sizning tasdiqlash kodinggiz. {vrf_code}',
               'from': '4546',
               }
    headers = {
        'Authorization':
            f"Bearer {SMS_TOKEN}"
    }
    requests.post(url=url, headers=headers, data=payload)
    # END SEND SMS

    await state.update_data({"vrf_code": vrf_code})

    await Registration.vrf_code.set()


@dp.message_handler(state=Registration.get_phone_number)
async def invalid_format_phone_number(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(global_file.INVALID_FORMAT_PHONE_NUMBER[data['language']])
    await Registration.get_phone_number.set()


@dp.message_handler(state=Registration.vrf_code)
async def get_vrf_code(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text == str(data['vrf_code']):

        r = requests.post(
            url="http://127.0.0.1:8000/bot/users/",
            data={
                'telegram_id': message.from_user.id,
                'phone_number': data['phone_number'],
                'telegram_username': message.from_user.username,
                'language': data['language']
            }
        )
        if r.status_code == 201:
            await home_page.home(message)
            await state.finish()
    else:
        await message.answer(global_file.VRF_CODE_ERROR_MESSAGE[data['language']])
