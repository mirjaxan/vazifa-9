from aiogram import Bot, Dispatcher
from database import env
from aiogram import Router
import asyncio
import logging


from handler import user_router


dp = Dispatcher ()

async def main():
    bot = Bot(env.str("TOKEN" ))
    dp.include_router(user_router)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())