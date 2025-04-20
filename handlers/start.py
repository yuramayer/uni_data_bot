from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import time
import datetime
from back.cloud import get_key, send_logs


start_router = Router()

@start_router.message(Command('start'))
async def cmd_start(message: Message):

    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    start = time.monotonic()
    user_id = message.chat.id

    user_message = message.text
    assert type(user_message) == str

    await message.answer('Привет! 🙋🏼‍♀️\n\nЗадай вопрос ChatGPT. '
                         'Прямо напрямую спрашивай!')
    

    working_ms = int((time.monotonic() - start) * 1000)

    log_json = {
        "timestamp": timestamp,
        "user_id": user_id,
        'type': 'start_cmd',
        "question": user_message,
        "bot_working_ms": working_ms,
        "answer": '[start_message]'
    }
    
    try:
        key = get_key(timestamp, user_id)

        send_logs(log_json, key)

    except Exception as err:
        await message.answer('При записи логов произошла ошибка 😔')
