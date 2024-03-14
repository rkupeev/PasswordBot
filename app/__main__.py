import logging
import asyncio
from aiogram import Bot, Dispatcher

from os import getenv

from handlers import greeting, create_password
from config import load_config

#py app/__main__.py

async def main():
    config = load_config()
    bot = Bot(token=config.token)

    logging.basicConfig(level=logging.DEBUG, filename="logs.log")

    dp = Dispatcher()
    dp.include_routers(
        greeting.router,
        create_password.router)
    

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
