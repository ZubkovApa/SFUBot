from aiogram import Router
from aiogram.types import Message
from keyboard import get_faq_keyboard, main_keyboard

# Создаем роутер
faq_router = Router()

# Меню FAQ
@faq_router.message(lambda message: message.text == '❓ Частые вопросы')
async def faq_menu(message: Message):
    await message.answer(
        "Выберите интересующий вас вопрос:",
        reply_markup=get_faq_keyboard()
    )

# Конкретные вопросы
@faq_router.message(lambda message: message.text == '💰 Стоимость курсов')
async def faq_price(message: Message):
    await message.answer(
        "💰 <b>Стоимость курсов</b>\n\n"
        "• Базовый курс: <b>25 000 руб.</b>\n"
        "• Продвинутый курс: <b>45 000 руб.</b>\n"
        "• Интенсив: <b>35 000 руб.</b>\n\n"
        "<i>Возможна рассрочка платежа на 3-6 месяцев.</i>",
        reply_markup=get_faq_keyboard()
    )

@faq_router.message(lambda message: message.text == '⏱️ Длительность обучения')
async def faq_duration(message: Message):
    await message.answer(
        "⏱️ <b>Длительность обучения</b>\n\n"
        "• Базовый курс: <b>2 месяца</b> (16 занятий)\n"
        "• Продвинутый курс: <b>4 месяца</b> (32 занятия)\n"
        "• Интенсив: <b>1 месяц</b> (ежедневные занятия)\n\n"
        "<i>Занятия проходят 2 раза в неделю по 3 часа.</i>",
        reply_markup=get_faq_keyboard()
    )

@faq_router.message(lambda message: message.text == '📅 Начало занятий')
async def faq_start(message: Message):
    await message.answer(
        "📅 <b>Начало занятий</b>\n\n"
        "Новые группы стартуют <b>каждый понедельник</b>.\n\n"
        "<i>Ближайшие даты начала:\n"
        "- 1 апреля\n"
        "- 8 апреля\n"
        "- 15 апреля</i>",
        reply_markup=get_faq_keyboard()
    )

@faq_router.message(lambda message: message.text == '🎓 Что нужно для обучения')
async def faq_requirements(message: Message):
    await message.answer(
        "🎓 <b>Что нужно для обучения</b>\n\n"
        "• Удобная одежда и обувь\n"
        "• Фартук (можно приобрести у нас)\n"
        "• Хорошее настроение!\n\n"
        "<i>Все продукты и оборудование мы предоставляем.</i>",
        reply_markup=get_faq_keyboard()
    )

    @faq_router.message(lambda message: message.text == '📞 Контакты')
    async def contacts_command(message: Message):
        contacts_text = """
    📞 <b>Связь с администратором</b>

    <b>Контактные данные:</b>
    👨‍💼 <b>Администратор:</b> Анна Петрова
    📞 <b>Телефон:</b> +7 (495) 765-43-21
    📧 <b>Email:</b> admin@gastroschool.ru
    💬 <b>Telegram:</b> @gastro_admin

    <b>Время для связи:</b>
    ⌚ Пн-Пт: 10:00 - 19:00
    ⌚ Суббота: 11:00 - 16:00
    🚫 Воскресенье: выходной
        """
        await message.answer(contacts_text, reply_markup=main_keyboard)

