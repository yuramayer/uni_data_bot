"""Help handler for the bot"""

import time
import datetime
from requests import RequestException
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from back.cloud import get_key, send_logs
from filters.admin_checker import IsAdmin
from config.conf import admins_ids


help_router = Router()
help_router.message.filter(
    IsAdmin(admins_ids)
)


@help_router.message(Command('help'))
async def cmd_help(message: Message):
    """Command 'help' for the admins"""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    start = time.monotonic()
    user_id = message.chat.id

    user_message = message.text
    assert isinstance(user_message, str)

    msg = (
        'Я - бот с ChatGPT 😉\n\nСпроси меня вопрос, '
        'и я постараюсь ответить.\n\n'
        'Разработчик: <b>@botrqst</b>'
    )
    await message.answer(msg)

    working_ms = int((time.monotonic() - start) * 1000)

    log_json = {
        "timestamp": timestamp,
        "user_id": user_id,
        'type': 'help_cmd',
        "question": user_message,
        "bot_working_ms": working_ms,
        "answer": '[help_message]'
    }

    try:
        key = get_key(timestamp, user_id)

        send_logs(log_json, key)

    except (ValueError, TypeError, KeyError, RequestException):
        await message.answer('При записи логов произошла ошибка 😔')
