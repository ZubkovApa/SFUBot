from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Заполнить анкету')],
        [
            KeyboardButton(text='Частые вопросы'),
            KeyboardButton(text='Связь с администратором')
        ],
        [
            KeyboardButton(text='ℹ️ О нас'),
            KeyboardButton(text='🔗 Полезные материалы')
        ]
    ],
    resize_keyboard=True
)

# Клавиатура для возврата
back_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='⬅️ Назад в меню')]
    ],
    resize_keyboard=True
)
