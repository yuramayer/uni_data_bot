"""Bot core objects module"""

import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from config import conf


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

bot = Bot(
    token=conf.BOT_TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))

dp = Dispatcher(storage=MemoryStorage())
