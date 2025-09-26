from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from buttons import REG_TEXT

user_router = Router()

@user_router.message(CommandStart())
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📝 Registration")]
        ],
        resize_keyboard=True
    )
    await message.answer(REG_TEXT, reply_markup=keyboard)

@user_router.message(lambda msg: msg.text == "📝 Registration")
async def registration(message: Message):
    await message.answer("Siz ro‘yxatdan o‘tish jarayonini boshladingiz ✅\nIltimos, ismingizni yuboring.")
