import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiogram.types import Message
from aiogram.filters import CommandStart
import logging

load_dotenv()


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Привет!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        print('Start')
        print('#############')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')