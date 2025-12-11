from aiogram import Router, types
from aiogram.filters import Command
from ..keyboards import main_menu
from ..db import user_exists

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    tg_id = message.from_user.id
    user = user_exists(tg_id)
    if user:
        await message.answer(
            'С возвращением!',
            reply_markup=main_menu()
        )
    else:
        await message.answer(
            'Привет! Я бот школы кулинарии, могу ответить на ваши вопросы и рассказать о наших программах. Давайте познакомимся?',
            reply_markup=main_menu()
        )

# Тест
