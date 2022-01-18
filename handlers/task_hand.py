from aiogram import types
from loader import dp
from keyboards.task4_kb import task_kb


@dp.message_handler(commands="items")
async def start_items(message: types.Message):
    await message.answer_photo(photo="https://domstrousam.ru/wp-content/uploads/2021/02/mandarin_gorchit.jpg",reply_markup=task_kb)