from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

header_menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇸🇱 O`zbekcha', callback_data='uz'),
            InlineKeyboardButton(text='🇷🇺 Ruscha', callback_data='ru'),
            InlineKeyboardButton(text='🇺🇸 Inglizcha', callback_data='us')
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
