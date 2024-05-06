from aiogram.types import InlineKeyboardMarkup, KeyboardButton, WebAppInfo

def web_app():
	return InlineKeyboardMarkup().add(KeyboardButton('open', web_app=WebAppInfo(url='...')))