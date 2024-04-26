import asyncio
import logging
import pymongo

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

local = 'mongodb://localhost:27017'
client = pymongo.MongoClient(local)
db = client['test']
col = db['feedbacks']

API_TOKEN = '7089693459:AAGOaGR191H7DGu55ItebS2fLUG3CaIXZz0'  # Токен бота
CHANNEL_ID = -1002012942904  # ID канала(в котором есть бот)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def send_message(channel_id: int, text: str):
    async with Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) as bot:
        try:
            await bot.send_message(channel_id, text)
        except Exception as e:
            logger.error(f"Failed to send message: {e}")


async def send_feedbacks():
    try:
        cursor = col.find({})
        for feedback in cursor:
            text = f"User: {feedback['user_nickname']}\n" \
                   f"Feedback: {feedback['text']}\n" \
                   f"Rating: {feedback['rating']}\n" \
                   f"Date: {feedback['date_time']}\n" \
                   f"Tags: {', '.join(feedback['tags'])}\n" \
                   f"Status: {feedback['status']}"
            await send_message(CHANNEL_ID, text)
    except Exception as e:
        logger.error(f"Failed to send feedbacks: {e}")


async def main():
    try:
        await send_feedbacks()
    finally:
        client.close()


if __name__ == '__main__':
    asyncio.run(main())
