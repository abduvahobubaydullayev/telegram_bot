from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

header_menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='πΈπ± O`zbekcha', callback_data='uz'),
            InlineKeyboardButton(text='π·πΊ Ruscha', callback_data='ru'),
            InlineKeyboardButton(text='πΊπΈ Inglizcha', callback_data='us')
        ],
    ],
)

buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='kontakt jo`natish', request_contact=True),
        ],
    ],
    resize_keyboard=True
)
