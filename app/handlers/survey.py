from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from ..keyboards import main_menu
from ..db import save_user, user_exists
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

@router.callback_query(lambda c: c.data == 'menu:survey')
async def start_survey(call: types.CallbackQuery, state: FSMContext):
    tg_id = call.from_user.id
    if user_exists(tg_id):
        await call.message.answer('Вы уже заполнили анкету.', reply_markup=main_menu())
        return
    await state.clear()
    await state.set_state(Survey.first_name)
    await call.message.answer('Пожалуйста, введите ваше имя (текстом):')

# Все остальные обработчики шагов (first_name → last_name → email → phone → city → level) идентичны предыдущей версии
# с сохранением данных через save_user и выводом main_menu() после завершения анкеты
