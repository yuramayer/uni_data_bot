import asyncio
from handlers import start, help, mes_reply
from bot import bot, dp
from utils.starting import on_startup


async def main():
    dp.include_routers(start.start_router, help.help_router,
                       mes_reply.reply_router)
    dp.startup.register(on_startup)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
