from bot import bot
from config.conf import admins_ids

async def on_startup():
    
    for admin_id in admins_ids:
        await bot.send_message(admin_id, 'Бот включён 😎')
