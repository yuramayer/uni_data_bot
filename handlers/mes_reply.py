"""Message reply for the admins"""

import time
import datetime
from requests import RequestException
from aiogram import Router, F
from aiogram.types import Message
from back.answer import create_answer
from back.cloud import get_key, send_logs
from filters.admin_checker import IsAdmin
from config.conf import admins_ids


reply_router = Router()
reply_router.message.filter(
    IsAdmin(admins_ids)
)


@reply_router.message(F.text)
async def bot_reply(message: Message):
    """Bot reply func for the bot"""

    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    start = time.monotonic()
    user_id = message.chat.id

    user_message = message.text
    assert isinstance(user_message, str)

    if len(user_message) > 500:
        answer_text = "Вопрос должен быть меньше 500 символов! 🙈"

    else:
        answer_text = create_answer(user_message)

    await message.answer(answer_text)

    working_ms = int((time.monotonic() - start) * 1000)

    log_json = {
        "timestamp": timestamp,
        "user_id": user_id,
        'type': 'gpt_question',
        "question": user_message,
        "bot_working_ms": working_ms,
        "answer": answer_text
    }

    try:
        key = get_key(timestamp, user_id)

        send_logs(log_json, key)

    except (ValueError, TypeError, KeyError, RequestException):
        await message.answer('При записи логов произошла ошибка 😔')
