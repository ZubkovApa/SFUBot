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
            KeyboardButton(text='📞 Связь с администратором')
        ]
    ],
    resize_keyboard=True
)

# Клавиатура FAQ (меню выбора вопроса)
def get_faq_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Ваш институт государственный или частный?')],
            [KeyboardButton(text='Предусмотрены ли бюджетные места для поступления?')],
            [KeyboardButton(text='Могу ли я обучаться заочно?')],
            [KeyboardButton(text='Что нужно для поступления?')],
            [KeyboardButton(text='⬅️ В главное меню')]
        ],
        resize_keyboard=True
    )

# Клавиатура материалов (меню выбора материала)
def get_links_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='📚 Образовательные программы')],
            [KeyboardButton(text='🍳 Наши соцсети')],
            [KeyboardButton(text='🌟 Дополнительные материалы')],
            [KeyboardButton(text='🏨 Ресторан #Истории')],
            [KeyboardButton(text='⬅️ В главное меню')]
        ],
        resize_keyboard=True
    )
