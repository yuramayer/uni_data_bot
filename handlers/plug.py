"""Plug for the non-admins"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from filters.admin_checker import NotAdmin
from config.conf import admins_ids


plug_router = Router()
plug_router.message.filter(
    NotAdmin(admins_ids)
)


@plug_router.message(F.text)
@plug_router.message(Command('start'))
async def plug_msg(message: Message):
    """Plug message for the non-admins"""

    msg = (
        'Я - бот с ChatGPT 😉\n\n'
        'Бот доступен для администраторов\n\n'
        'Разработчик: <b>@botrqst</b>'
    )
    await message.answer(msg)
