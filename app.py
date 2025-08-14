"""Main aiogram bot app"""

import asyncio
from handlers import (
    start_router,
    help_router,
    reply_router,
    plug_router
)
from bot import bot, dp
from utils.starting import on_startup


async def main():
    """Base bot func"""
    dp.include_routers(
        start_router,
        help_router,
        reply_router,
        plug_router
    )
    dp.startup.register(on_startup)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
