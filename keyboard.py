from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню (только для тех, кто заполнил анкету)
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='❓ Частые вопросы'),
            KeyboardButton(text='🔗 Полезные материалы')
        ],
        [
            KeyboardButton(text='ℹ️ О нас'),
            KeyboardButton(text='📞 Контакты')
        ]
    ],
    resize_keyboard=True
)

# Клавиатура FAQ (меню выбора вопроса)
def get_faq_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='💰 Стоимость курсов')],
            [KeyboardButton(text='⏱️ Длительность обучения')],
            [KeyboardButton(text='📅 Начало занятий')],
            [KeyboardButton(text='🎓 Что нужно для обучения')],
            [KeyboardButton(text='⬅️ В главное меню')]
        ],
        resize_keyboard=True
    )

# Клавиатура материалов (меню выбора материала)
def get_links_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='📚 Учебные материалы')],
            [KeyboardButton(text='🍳 Практические задания')],
            [KeyboardButton(text='🌟 Дополнительные ресурсы')],
            [KeyboardButton(text='🏨 Партнеры школы')],
            [KeyboardButton(text='⬅️ В главное меню')]
        ],
        resize_keyboard=True
    )
