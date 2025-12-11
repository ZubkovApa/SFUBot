import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties  # НОВЫЙ ИМПОРТ

from config import BOT_TOKEN
from keyboard import main_keyboard
from db import Database
from links import links_router

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
# ИСПРАВЛЕННЫЙ СИНТАКСИС ДЛЯ aiogram 3.7+
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # ТАК ТЕПЕРЬ!
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
async def cmd_start(message: Message):
    user_id = message.from_user.id

    if db.user_exists(user_id):
        await message.answer(
            "🎓 Добро пожаловать в Школу Гастрономии!\n\n"
            "Выберите действие на клавиатуре ниже:",
            reply_markup=main_keyboard
        )
    else:
        await message.answer(
            "👋 Приветствуем в Школе Гастрономии!\n\n"
            "Для записи на курс заполните, пожалуйста, небольшую анкету.\n\n"
            "Нажмите кнопку 'Заполнить анкету' или напишите /survey",
            reply_markup=main_keyboard
        )


# Обработка кнопок главного меню
@dp.message(lambda message: message.text == 'Заполнить анкету')
async def handle_survey_button(message: Message):
    user_id = message.from_user.id

    if db.user_exists(user_id):
        await message.answer(
            "📋 Вы уже заполняли анкету ранее!\n"
            "Если нужно изменить данные, свяжитесь с администратором.",
            reply_markup=main_keyboard
        )
    else:
        # Отправляем пользователя на анкету
        await message.answer(
            "Для заполнения анкеты используйте команду /survey",
            reply_markup=ReplyKeyboardRemove()
        )


# Обработка кнопки "Назад в меню"
@dp.message(lambda message: message.text == '⬅️ Назад в меню')
async def handle_back_button(message: Message):
    await message.answer("Возвращаю в главное меню:", reply_markup=main_keyboard)


# Запуск бота
async def main():
    logger.info("🚀 Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
