from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    """Главное меню бота (кнопки ReplyKeyboard)."""
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='❓ FAQ')],
            [KeyboardButton(text='📝 Заполнить анкету')],
            [KeyboardButton(text='📞 Контакты администратора')]
        ],
        resize_keyboard=True
    )
    return kb

def faq_keyboard(faq_items):
    """Inline клавиатура для FAQ."""
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=q, callback_data=f'faq:{qid}')] for qid, q in faq_items
        ]
    )
    return kb
