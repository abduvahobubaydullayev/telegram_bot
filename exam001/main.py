"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from config import *
from buttons import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print(message.text)
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Tilni tanlang!!!", reply_markup=header_menu1)


@dp.callback_query_handler(text="uz")
async def menu_tanlash(call: CallbackQuery):
    print(call)
    await call.message.answer(f'<b>Assalomu aleykum!!!</b>', parse_mode='HTML')
    print(call)


@dp.message_handler()
async def create(message: types.Message):
    print(message)
    await message.answer(message)


#
# @dp.message_handler()
# async def echo(message: types.Message):
#     print(message.text)
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)
#

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
