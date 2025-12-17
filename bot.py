import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext

from config import BOT_TOKEN
from keyboard import main_keyboard
from db import Database

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Инициализация БД
db = Database('db.sqlite')
db.create_table()

# Импорт роутеров
from survey import survey_router
from faq import faq_router
from about import about_router
from links import links_router

# Включение роутеров
dp.include_router(survey_router)
dp.include_router(faq_router)
dp.include_router(about_router)
dp.include_router(links_router)


# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id

    if db.user_exists(user_id):
        await message.answer(
            "🌟 <b>С возвращением в Институт Гастрономии!</b>\n\n"
            "Рады снова вас видеть! Чем могу помочь?",
            reply_markup=main_keyboard
        )
    else:
        await message.answer(
            "🎊 <b>Добро пожаловать в мир кулинарного мастерства!</b>\n\n"
            "Мы очень рады, что вы решили присоединиться к нашей школе!\n\n"
            "✨ <b>Для начала давайте познакомимся поближе.</b>\n"
            "Заполните небольшую анкету — это откроет все возможности этого бота!\n\n"
            "<i>Начнем? Это займет всего пару минут! 💫</i>",
            reply_markup=ReplyKeyboardRemove()
        )

        from survey import Survey
        await state.set_state(Survey.first_name)
        await message.answer("💬 <b>Как вас зовут?</b>\n"
            "<i>Напишите свое имя</i>")


# Обработка кнопки "Назад в меню"
@dp.message(lambda message: message.text == '⬅️ В главное меню')
async def handle_back_button(message: Message):
    await message.answer("Главное меню:", reply_markup=main_keyboard)


# Запуск бота
async def main():
    logger.info("🚀 Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
