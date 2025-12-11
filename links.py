from aiogram import Router
from aiogram.types import Message
from keyboard import get_links_keyboard

# Создаем роутер
links_router = Router()

# Меню материалов
@links_router.message(lambda message: message.text == '🔗 Полезные материалы')
async def links_menu(message: Message):
    await message.answer(
        "Выберите категорию материалов:",
        reply_markup=get_links_keyboard()
    )

# Конкретные материалы
@links_router.message(lambda message: message.text == '📚 Учебные материалы')
async def links_study(message: Message):
    await message.answer(
        "📚 <b>Учебные материалы</b>\n\n"
        "• <a href='https://example.com/basics.pdf'>Основы кулинарии (PDF)</a>\n"
        "• <a href='https://youtube.com/playlist?list=example'>Видеокурс по ножам</a>\n"
        "• <a href='https://example.com/spices'>Энциклопедия специй</a>",
        disable_web_page_preview=False,
        reply_markup=get_links_keyboard()
    )

@links_router.message(lambda message: message.text == '🍳 Практические задания')
async def links_practice(message: Message):
    await message.answer(
        "🍳 <b>Практические задания</b>\n\n"
        "• <a href='https://example.com/checklist'>Чек-лист повара</a>\n"
        "• <a href='https://example.com/seasonal'>Сезонные продукты</a>\n"
        "• <a href='https://example.com/templates'>Шаблоны рецептов</a>",
        disable_web_page_preview=False,
        reply_markup=get_links_keyboard()
    )

@links_router.message(lambda message: message.text == '🌟 Дополнительные ресурсы')
async def links_extra(message: Message):
    await message.answer(
        "🌟 <b>Дополнительные ресурсы</b>\n\n"
        "• <a href='https://example.com/blog'>Блог преподавателей</a>\n"
        "• <a href='https://example.com/webinars'>Бесплатные вебинары</a>\n"
        "• <a href='https://example.com/tests'>Тесты на профориентацию</a>",
        disable_web_page_preview=False,
        reply_markup=get_links_keyboard()
    )

@links_router.message(lambda message: message.text == '🏨 Партнеры школы')
async def links_partners(message: Message):
    await message.answer(
        "🏨 <b>Партнеры школы</b>\n\n"
        "• Ресторан 'Le Chef' - скидка 10% для студентов\n"
        "• Магазин 'ПрофКухня' - спеццены на оборудование\n"
        "• Винный клуб 'Sommelier' - бесплатные дегустации",
        reply_markup=get_links_keyboard()
    )
