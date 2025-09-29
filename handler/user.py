import json
import os
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from buttons.user import register_kb, main_menu_kb, menu_kb, search_kb
from buttons.user_text import *

user_router = Router()
USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def is_registered(user_id):
    users = load_users()
    return any(u["id"] == user_id for u in users)


# --- FSM uchun class ---
class RegisterForm(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()


@user_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    if is_registered(message.from_user.id):
        await message.answer(ALREADY_REGISTERED, reply_markup=main_menu_kb)
    else:
        await message.answer(REG_TEXT, reply_markup=register_kb)


# --- Registratsiya boshlanishi ---
@user_router.message(F.text == "📝 Registration")
async def registration(message: Message, state: FSMContext):
    await state.set_state(RegisterForm.first_name)
    await message.answer("Ismingizni kiriting:", reply_markup=ReplyKeyboardRemove())


@user_router.message(RegisterForm.first_name)
async def get_first_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(RegisterForm.last_name)
    await message.answer("Familyangizni kiriting:")


@user_router.message(RegisterForm.last_name)
async def get_last_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(RegisterForm.phone)

    phone_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]
        ],
        resize_keyboard=True
    )

    await message.answer("Telefon raqamingizni yuboring:", reply_markup=phone_kb)


@user_router.message(RegisterForm.phone)
async def get_phone(message: Message, state: FSMContext):
    data = await state.get_data()

    phone = message.contact.phone_number if message.contact else message.text

    user = {
        "id": message.from_user.id,
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "phone": phone
    }

    users = load_users()
    users.append(user)
    save_users(users)

    await state.clear()
    await message.answer("Ro‘yxatdan muvaffaqiyatli o‘tdingiz ✅", reply_markup=main_menu_kb)


# --- Asosiy tugmalar handlerlari ---
@user_router.message(F.text == "📖 Menu")
async def menu_handler(message: Message):
    await message.answer(MENU_TEXT, reply_markup=menu_kb)

@user_router.message(F.text == "🛒 Order")
async def order_handler(message: Message):
    await message.answer(ORDER_TEXT)

@user_router.message(F.text == "☎️ Contact")
async def contact_handler(message: Message):
    await message.answer(CONTACT_TEXT)

@user_router.message(F.text == "🔍 Search")
async def search_handler(message: Message):
    await message.answer(SEARCH_TEXT, reply_markup=search_kb)

@user_router.message(F.text == "🆕 New")
async def new_handler(message: Message):
    await message.answer(NEW_TEXT)

@user_router.message(F.text == "💸 Discount")
async def discount_handler(message: Message):
    await message.answer(DISCOUNT_TEXT)

@user_router.message(F.text == "📚 All")
async def all_handler(message: Message):
    await message.answer(ALL_TEXT)

@user_router.message(F.text == "📂 Genre")
async def genre_handler(message: Message):
    await message.answer(GENRE_TEXT)

@user_router.message(F.text == "✍️ Author")
async def author_handler(message: Message):
    await message.answer(AUTHOR_TEXT)

@user_router.message(F.text == "📖 Title")
async def title_handler(message: Message):
    await message.answer(TITLE_TEXT)

@user_router.message(F.text == "⬅️ Back")
async def back_handler(message: Message):
    await message.answer(BACK_TEXT, reply_markup=main_menu_kb)
