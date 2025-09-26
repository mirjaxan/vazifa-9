from aiogram.types import Message
from aiogram import router
from aiogram.filters import CommandStart,Command
from buttons import REG_TEXT

user_router = router()


@user_router.message(CommandStart())
async def start(message: Message):
    await message.answer(text)