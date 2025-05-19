from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from database.database import db_tables, users_repo
from keyboards.reply import start_keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    db_tables.create_tables()
    if users_repo.get_user(chat_id=message.from_user.id) is None:
        users_repo.add_user(chat_id=message.from_user.id)
        print(f'user with chat_id={message.from_user.id} was added')

    await message.answer(
        text='<b>Добро пожаловать\nВас приветствует бот ресторана "TastyFood"\nВыберите действия ниже</b>',
        reply_markup=start_keyboard(),
        parse_mode='HTML'
    )