from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, CommandObject

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет!', reply_markup=kb.start)