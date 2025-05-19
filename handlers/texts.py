from aiogram import Router, F
from aiogram.types import Message

from keyboards.inline import categories_keyboard, get_purchases_kb, get_history_kb

router = Router()

@router.message(F.text == 'Меню')
async def get_menu(message: Message) -> None:
    await message.answer(
        text='<b>Выберите категорию из перечисленных ниже</b>',
        parse_mode='HTML',
        reply_markup=categories_keyboard()
    )

@router.message(F.text == 'Корзина')
async def get_purchases(message: Message) -> None:
    data, inline_kb = get_purchases_kb(chat_id=message.from_user.id)

    if data is None:
        await message.delete()
        return await message.answer(
            text='У вас пустая корзина'
        )

    await message.answer(
        text='<b>В корзину вы положили следующие товары</b>',
        parse_mode='HTML'
    )

    await message.answer_photo(
        caption=f'<b>🍲Название:</b> {data[1]}\n<b>💸Цена:</b> {data[2]}',
        parse_mode='HTML',
        reply_markup=inline_kb,
        photo=data[3]
    )

@router.message(F.text.lower() == 'история заказов')
async def get_purchases_history(message: Message) -> None:
    data, inline_kb = get_history_kb(chat_id=message.from_user.id)

    print(data)
    await message.answer(
        text='<b>Ваша история заказов</b>',
        parse_mode='HTML'
    )

    await message.answer_photo(
        caption=f'<b>🍲Название:</b> {data[0]}\n<b>💸Цена:</b> {data[1]} сум',
        parse_mode='HTML',
        reply_markup=inline_kb,
        photo=data[2]
    )