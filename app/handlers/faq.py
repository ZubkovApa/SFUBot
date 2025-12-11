from aiogram import Router, types
from aiogram.types import CallbackQuery
from ..keyboards import faq_keyboard, main_menu

router = Router()

# Статичные FAQ — можно вынести в БД
FAQ = [
    (1, 'Какие курсы есть?'),
    (2, 'Где проходят занятия?'),
    (3, 'Стоимость курса и расписание'),
]

FAQ_ANSWERS = {
    1: 'У нас есть курсы для начинающих и продвинутых. Подробнее: https://example.com/courses',
    2: 'Занятия проходят в центре города, адрес: ул. Примерная, 1. Смотрите карту: https://example.com/contacts',
    3: 'Стоимость зависит от уровня и формата. Свяжитесь с менеджером или заполните анкету для точной информации.'
}

@router.message(lambda message: message.text == '❓ FAQ')
async def show_faq(message: types.Message):
    """Показать список FAQ с inline кнопками."""
    await message.answer('Часто задаваемые вопросы:', reply_markup=faq_keyboard(FAQ))

@router.callback_query(lambda c: c.data and c.data.startswith('faq:'))
async def on_faq(call: CallbackQuery):
    """Обработка выбора конкретного вопроса FAQ."""
    await call.answer()  # убрать loader
    qid = int(call.data.split(':', 1)[1])
    question = dict(FAQ).get(qid, 'Вопрос не найден.')
    answer = FAQ_ANSWERS.get(qid, 'Ответ не найден.')
    await call.message.edit_text(f'*Вопрос:* {question}\n\n*Ответ:* {answer}', parse_mode='Markdown')

@router.callback_query(lambda c: c.data == 'back:menu')
async def back_to_menu(call: CallbackQuery):
    """Возврат в главное меню."""
    await call.answer()
    await call.message.edit_text('Выберите действие:', reply_markup=main_menu())

@router.message(lambda message: message.text == '📞 Контакты администратора')
async def contacts_admin(message: types.Message):
    """Показ контактов администратора."""
    await message.answer('Для связи с администратором: +7 900 000-00-00 или admin@example.com')


# Тест
