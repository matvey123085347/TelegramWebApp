from aiogram import Bot, executor, Dispatcher
from asiogram.types import Message, CallbackQuery
import asyncio
from keyboards import *

bot = Bot(token='5771600757:AAGSIUfluDBKQP209GfQrB-mDI9WwyhmtcI', parse_mode='HTML')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['text'])
async def main_app(message: Message):
	await message.answer('hello', reply_markup=web_app())

@dp.message_handler(content_types='web_app_data')
async def web_data(web_msg, msg: Message):
	print(web_msg)

