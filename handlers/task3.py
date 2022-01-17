from loader import dp
from aiogram import types
from keyboards.test import testing_kb
from keyboards.callbackdatas import testing


@dp.message_handler(commands='inline_buttons_1')
async def test(message: types.Message):
    await message.answer(f'''Edit @Sberleadbot info.
Name: Бот для Заданий на Курсе Udemy
Description: ?
About: ?
Botpic: ? no botpic
Commands: no commands yet''', reply_markup=testing_kb)