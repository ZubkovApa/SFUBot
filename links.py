from aiogram import Router
from aiogram.types import Message
from keyboard import get_links_keyboard

# Создаем роутер
links_router = Router()

# Меню материалов
@links_router.message(lambda message: message.text == '🔗 Полезные материалы')
async def links_menu(message: Message):
    await message.answer(
        "Выберите категорию:",
        reply_markup=get_links_keyboard()
    )

# Конкретные материалы
@links_router.message(lambda message: message.text == '📚 Образовательные программы')
async def links_study(message: Message):
    await message.answer(
        "📚 <b>Образовательные программы:</b>\n\n"
        "<a href='https://gastronomyinstitute.ru/vshg'>🍳 Высшая школа гастрономии от\nINSTITUT LYFE EXECUTIVE EDUCATION</a>\n"
        "<a href='https://gastronomyinstitute.ru/vshrm'>👤 Высшая школа ресторанного менеджмента</a>\n"
        "<a href='https://gastronomyinstitute.ru/vshki'>🎂 Высшая школа кондитерского искусства</a>\n"
        "<a href='https://gastronomyinstitute.ru/vshom'>🏢 Высшая школа отельного менеджмента</a>\n"
        "<a href='https://gastronomyinstitute.ru/st'>👓 Стратегическое управление в индустрии гостеприимства</a>",
        disable_web_page_preview=True,
        reply_markup=get_links_keyboard()
    )

@links_router.message(lambda message: message.text == '🛜 Наши соцсети')
async def links_practice(message: Message):
    await message.answer(
        "🍳 <b>Наши соцсети:</b>\n\n"
        "• <a href='https://t.me/gastronomy_inst'>Telegram</a>\n"
        "• <a href='https://vk.com/gastronomy_inst'>ВКонтакте</a>\n"
        "• <a href='https://www.youtube.com/@gastronomyinstitute/featured'>Youtube</a>\n"
        "• <a href='https://rutube.ru/channel/24798940/'>Rutube</a>\n"
        "• <a href='https://gastronomyinstitute.ru/'>Официальный сайт</a>",
        disable_web_page_preview=True,
        reply_markup=get_links_keyboard()
    )

@links_router.message(lambda message: message.text == '🌟 Дополнительные материалы')
async def links_extra(message: Message):
    await message.answer(
        "🌟 <b>Дополнительные материалы:</b>\n\n"
        "• <a href='https://gastronomyinstitute.ru/dop-o'>Наши курсы</a>\n"
        "• <a href='https://gastronomyinstitute.ru/partners'>Партнеры института</a>\n"
        "• <a href='https://gastronomyinstitute.ru/for_abiturients'>Информация для абитуриентов</a>\n"
        "• <a href='https://disk.360.yandex.ru/d/Mw8p66rrJjc4og'>Дайджесты</a>",
        disable_web_page_preview=True,
        reply_markup=get_links_keyboard()
    )

@links_router.message(lambda message: message.text == '🏨 Ресторан #Истории')
async def links_partners(message: Message):
    await message.answer(
        "🏨 <b>Ресторан #Истории:</b>\n\n"
        "• <a href='https://storiesrest.ru/'>Официальный сайт</a>\n"
        "• <a href='https://vk.com/istoree.rest'>ВКонтакте</a>\n"
        "• <a href='https://disk.360.yandex.ru/i/pGapRTzrT-s8_g'>Меню ресторана</a>",
        disable_web_page_preview=True,
        reply_markup=get_links_keyboard()
    )
