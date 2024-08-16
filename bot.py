import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv('TG_API_KEY'))

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я твой новый бот.")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Я могу помочь тебе с командами:\n/start - Запустить бота\n/help - Показать это сообщение")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())