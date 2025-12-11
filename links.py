from aiogram import Router
from aiogram.types import Message
from keyboard import back_keyboard, main_keyboard

# Создаем роутер
links_router = Router()

@links_router.message(lambda message: message.text == '🔗 Полезные материалы')
async def links_command(message: Message):
    links_text = """
🔗 <b>Полезные материалы и ссылки</b>

<b>Учебные материалы:</b>
📚 <a href="https://example.com/basics.pdf">Основы кулинарии (PDF учебник)</a>
🎬 <a href="https://youtube.com/playlist?list=example">Видеокурс "Техника работы с ножами"</a>
📖 <a href="https://example.com/spices">Энциклопедия специй и приправ</a>

<b>Для практики:</b>
🍳 <a href="https://example.com/checklist">Чек-лист начинающего повара</a>
🥦 <a href="https://example.com/seasonal">Сезонный календарь продуктов</a>
📋 <a href="https://example.com/templates">Шаблоны рецептов для тренировки</a>

<b>Дополнительные ресурсы:</b>
🌟 <a href="https://example.com/blog">Блог наших преподавателей</a>
🎓 <a href="https://example.com/webinars">Бесплатные вебинары</a>
📊 <a href="https://example.com/tests">Тесты на профориентацию</a>
    """
    await message.answer(links_text, disable_web_page_preview=False, reply_markup=back_keyboard)

@links_router.message(lambda message: message.text == '⬅️ Назад в меню')
async def back_to_menu(message: Message):
    await message.answer("Возвращаю в главное меню:", reply_markup=main_keyboard)
