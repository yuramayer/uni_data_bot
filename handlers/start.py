"""Start command handler for the admins"""

import time
import datetime
from requests import RequestException
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from back.cloud import get_key, send_logs
from filters.admin_checker import IsAdmin
from config.conf import admins_ids


start_router = Router()
start_router.message.filter(
    IsAdmin(admins_ids)
)


@start_router.message(Command('start'))
async def cmd_start(message: Message):
    """Admin sends /start to the bot"""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    start = time.monotonic()
    user_id = message.chat.id

    user_message = message.text
    assert isinstance(user_message, str)

    await message.answer(
        'Привет! 🙋🏼‍♀️\n\nЗадай вопрос ChatGPT. '
        'Прямо напрямую спрашивай!'
        )

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

    except (ValueError, TypeError, KeyError, RequestException):
        await message.answer('При записи логов произошла ошибка 😔')
