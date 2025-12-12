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
from survey import Survey  # Импортируем состояния анкеты

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


# Команда /startё
@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id

    if db.user_exists(user_id):
        # Пользователь уже заполнил анкету - показываем главное меню
        await message.answer(
            "🎓 С возвращением!\n\n"
            "Выберите действие:",
            reply_markup=main_keyboard
        )
    else:
        # Новый пользователь - сразу запускаем анкету
        await message.answer(
            "👋 Приветствуем в Школе Гастрономии!\n\n"
            "Для начала работы заполните, пожалуйста, анкету.\n"
            "Это займет всего 2 минуты!",
            reply_markup=ReplyKeyboardRemove()
        )

        # Устанавливаем первое состояние анкеты
        await state.set_state(Survey.first_name)
        await message.answer("Введите ваше имя:")


# Главное меню после анкеты
@dp.message(lambda message: message.text == '⬅️ В главное меню')
async def back_to_main_menu(message: Message):
    await message.answer("Главное меню:", reply_markup=main_keyboard)


# Запуск бота
async def main():
    logger.info("🚀 Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
