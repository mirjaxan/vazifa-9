import json, os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from buttons.admin import admin_main_kb, admin_menu_kb, add_book_kb, admin_order_kb
from buttons.user_text import *

import os
from dotenv import load_dotenv

load_dotenv()
ADMIN_ID = 2007554600


admin_router = Router()
BOOKS_FILE = "books.json"

# Kitoblarni yuklash/saqlash funksiyasi
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)


# --- FSM for book adding ---
class AddBook(StatesGroup):
    title = State()
    author = State()
    genre = State()
    year = State()
    price = State()


# --- Admin panel start ---
@admin_router.message(Command("admin"))
async def admin_start(message: Message):
    await message.answer(ADMIN_PANEL_TEXT, reply_markup=admin_main_kb)


@admin_router.message(Command("admin"))
async def admin_start(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer(ADMIN_PANEL_TEXT, reply_markup=admin_main_kb)
    else:
        await message.answer("❌ Sizda admin panelga ruxsat yo‘q!")



# --- Menu bo‘limi ---
@admin_router.message(F.text == "📖 Menu")
async def admin_menu(message: Message):
    await message.answer(MENU_ADMIN_TEXT, reply_markup=admin_menu_kb)


# --- Add jarayoni ---
@admin_router.message(F.text == "➕ Add")
async def add_start(message: Message, state: FSMContext):
    await state.set_state(AddBook.title)
    await message.answer(ADD_START_TEXT)


@admin_router.message(AddBook.title)
async def add_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(AddBook.author)
    await message.answer("Muallifni kiriting:")


@admin_router.message(AddBook.author)
async def add_author(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await state.set_state(AddBook.genre)
    await message.answer("Janrni kiriting:")


@admin_router.message(AddBook.genre)
async def add_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(AddBook.year)
    await message.answer("Yilni kiriting:")


@admin_router.message(AddBook.year)
async def add_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(AddBook.price)
    await message.answer("Narxni kiriting:")


@admin_router.message(AddBook.price)
async def add_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Ma’lumotlarni saqlash uchun 💾 Save tugmasini bosing", reply_markup=add_book_kb)


# --- Save tugmasi ---
@admin_router.message(F.text == "💾 Save")
async def save_book(message: Message, state: FSMContext):
    data = await state.get_data()
    books = load_books()
    books.append(data)
    save_books(books)

    await state.clear()
    text = (
        f"{BOOK_SAVED_TEXT}\n\n"
        f"📖 Nom: {data['title']}\n"
        f"✍️ Muallif: {data['author']}\n"
        f"📂 Janr: {data['genre']}\n"
        f"📅 Yil: {data['year']}\n"
        f"💵 Narx: {data['price']}"
    )
    await message.answer(text, reply_markup=admin_menu_kb)


# --- Order bo‘limi ---
@admin_router.message(F.text == "🛒 Order")
async def admin_order(message: Message):
    await message.answer(ORDER_ADMIN_TEXT, reply_markup=admin_order_kb)


@admin_router.message(F.text == "🆕 New")
async def new_order(message: Message):
    await message.answer("Yangi buyurtmalar hozircha yo‘q.")


@admin_router.message(F.text == "🔄 In Progress")
async def in_progress_order(message: Message):
    await message.answer("Jarayondagi buyurtmalar.")


@admin_router.message(F.text == "📚 All")
async def all_order(message: Message):
    await message.answer("Barcha buyurtmalar ro‘yxati.")


@admin_router.message(F.text == "✏️ Update")
async def update_order(message: Message):
    await message.answer("Buyurtmalarni yangilash funksiyasi.")


@admin_router.message(F.text == "❌ Delete")
async def delete_order(message: Message):
    await message.answer("Buyurtmalarni o‘chirish funksiyasi.")



@admin_router.message(F.text == "📊 Dashboard")
async def dashboard(message: Message):
    books = load_books()
    text = f"{DASHBOARD_TEXT}\n\n📚 Kitoblar soni: {len(books)}\n🛒 Buyurtmalar: 0"
    await message.answer(text)
