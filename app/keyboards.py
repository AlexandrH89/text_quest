from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Пробуждение в темноте')]
],
                resize_keyboard=True,
                input_field_placeholder='Выберите пунтк меню.')