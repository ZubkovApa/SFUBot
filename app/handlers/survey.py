from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.keyboards import main_menu
from app.db import save_user, user_exists
import re

router = Router()

class Survey(StatesGroup):
    first_name = State()
    last_name = State()
    email = State()
    phone = State()
    city = State()
    level = State()

PHONE_RE = re.compile(r"^\+?\d{7,15}$")

@router.message(lambda message: message.text == '📝 Заполнить анкету')
async def start_survey(message: types.Message, state: FSMContext):
    tg_id = message.from_user.id
    if user_exists(tg_id):
        await message.answer('Вы уже заполнили анкету. Если хотите обновить данные — свяжитесь с администратором.', reply_markup=main_menu())
        return
    await state.clear()
    await state.set_state(Survey.first_name)
    await message.answer('Пожалуйста, введите ваше имя')

@router.message(Survey.first_name)
async def process_first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text.strip())
    await state.set_state(Survey.last_name)
    await message.answer('Введите вашу фамилию')

@router.message(Survey.last_name)
async def process_last_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text.strip())
    await state.set_state(Survey.email)
    await message.answer('Введите ваш email:')

@router.message(Survey.email)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text.strip()
    # Базовая валидация — можно расширить
    if email and ('@' not in email or '.' not in email):
        await message.answer('Пожалуйста, введите корректный email')
        return
    await state.update_data(email=email)
    await state.set_state(Survey.phone)
    await message.answer('Введите номер телефона:')

@router.message(Survey.phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text.strip()
    if not PHONE_RE.match(phone):
        await message.answer('Некорректный номер. Введите номер в формате +79161234567')
        return
    await state.update_data(phone=phone)
    await state.set_state(Survey.city)
    await message.answer('Введите ваш город:')

@router.message(Survey.city)
async def process_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text.strip())
    await state.set_state(Survey.level)
    await message.answer('Введите ваш курс')

@router.message(Survey.level)
async def process_level(message: types.Message, state: FSMContext):
    await state.update_data(level=message.text.strip())
    data = await state.get_data()
    tg_id = message.from_user.id
    data['tg_id'] = tg_id
    # Сохраняем только при полном заполнении
    save_user(data)
    await state.clear()
    await message.answer('Спасибо! Ваша анкета сохранена', reply_markup=main_menu())

@router.message(lambda message: message.text == '/cancel')
async def cancel_cmd(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Опрос отменён.', reply_markup=main_menu())

# Тест
