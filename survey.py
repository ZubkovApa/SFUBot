from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from keyboard import main_keyboard
from db import Database

# Создаем роутер
survey_router = Router()


# Состояния для анкеты
class Survey(StatesGroup):
    first_name = State()
    last_name = State()
    email = State()
    phone = State()
    city = State()
    course = State()


# Обработчик имени
@survey_router.message(Survey.first_name)
async def process_first_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Survey.last_name)
    await message.answer("Введите вашу фамилию:")


# Обработчик фамилии
@survey_router.message(Survey.last_name)
async def process_last_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Survey.email)
    await message.answer("Введите ваш email:")


# Обработчик email
@survey_router.message(Survey.email)
async def process_email(message: Message, state: FSMContext):
    # Простая валидация email
    if '@' not in message.text or '.' not in message.text:
        await message.answer("Пожалуйста, введите корректный email (например: example@mail.com):")
        return

    await state.update_data(email=message.text)
    await state.set_state(Survey.phone)
    await message.answer("Введите ваш номер телефона:")


# Обработчик телефона
@survey_router.message(Survey.phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Survey.city)
    await message.answer("Введите ваш город:")


# Обработчик города
@survey_router.message(Survey.city)
async def process_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Survey.course)

    # Клавиатура для выбора курса
    course_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🍳 Основы кулинарии")],
            [KeyboardButton(text="🎂 Кондитерское искусство")],
            [KeyboardButton(text="🍷 Искусство сомелье")],
            [KeyboardButton(text="🥘 Профессиональная кухня")]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите интересующий вас курс:", reply_markup=course_keyboard)


# Обработчик курса и завершение анкеты
@survey_router.message(Survey.course)
async def process_course(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    data = await state.get_data()
    user_id = message.from_user.id

    # Сохраняем в БД
    db = Database('db.sqlite')
    db.add_user(
        user_id=user_id,
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone=data['phone'],
        city=data['city'],
        course=data['course']
    )

    result_text = (
        f"✅ <b>Спасибо, {data['first_name']}! Анкета успешно заполнена!</b>\n\n"
        f"<b>Ваши данные:</b>\n"
        f"👤 <b>Имя:</b> {data['first_name']}\n"
        f"👤 <b>Фамилия:</b> {data['last_name']}\n"
        f"📧 <b>Email:</b> {data['email']}\n"
        f"📞 <b>Телефон:</b> {data['phone']}\n"
        f"🏙️ <b>Город:</b> {data['city']}\n"
        f"🎓 <b>Курс:</b> {data['course']}\n\n"
        f"<i>Администратор свяжется с вами в течение 24 часов для подтверждения записи.</i>\n\n"
        f"Теперь вам доступны все функции бота!"
    )

    await message.answer(result_text, reply_markup=main_keyboard)
    await state.clear()
