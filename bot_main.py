from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import logging
import sys
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from token_data import TOKEN
from quiz import quiz_router
from info import about

dp = Dispatcher()
dp.include_router(quiz_router)
bot = Bot(TOKEN)

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    await state.clear()
    keyboard = ReplyKeyboardBuilder()
    keyboard.row(types.KeyboardButton(text='Пройти викторину'), types.KeyboardButton(text='Связаться с сотрудником'))
    keyboard.row(types.KeyboardButton(text='Узнать о программе опеки'))

    await message.answer(f"Доброго времени суток! Это телеграм-бот <a href='https://moscowzoo.ru/'>Московского зоопарка</a>.\n\nЯ смогу определить ваше тотемное животное, а также помочь связаться с сотрудником нашего зоопарка.\n\nПеред тем как проходить викторину, рекомендую ознакомиться с нашей программой опеки животных", parse_mode='HTML', reply_markup=keyboard.as_markup())


@dp.message(F.text == 'Узнать о программе опеки')
async def description(message: Message):
    await message.answer(about)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())