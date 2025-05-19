from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InputMediaPhoto

from database.database import purchases_repo

from keyboards.inline import (
    categories_keyboard,
    get_purchases_kb,
    get_history_kb
)

router = Router()

@router.callback_query(F.data.startswith('prev'))
async def prev_categories(call: CallbackQuery) -> None:
    _, start, finish, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)
    
    await call.message.edit_reply_markup(
        reply_markup=categories_keyboard(start=int(start) - 5, finish=int(finish) - 5, current_page=int(page) - 1)
    )

@router.callback_query(F.data.startswith('next'))
async def next_categories(call: CallbackQuery) -> None:
    _, start, finish, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)
    
    await call.message.edit_reply_markup(
        reply_markup=categories_keyboard(start=int(start) + 5, finish=int(finish) + 5, current_page=int(page) + 1)
    )

@router.callback_query(F.data == 'home')
async def get_home(call: CallbackQuery) -> None:
    await call.message.delete()
    await call.message.answer(
        text='<b>Выберите категорию из перечисленных ниже</b>',
        parse_mode='HTML',
        reply_markup=categories_keyboard()
    )

@router.callback_query(F.data.contains('del_from_bask'))
async def delete_food_from_basket(call: CallbackQuery) -> None:
    _, id = call.data.split(':')
    data, inline_kb = get_purchases_kb(chat_id=call.from_user.id)

    purchases_repo.delete_one_product(chat_id=call.from_user.id, id=id)
    await call.answer(
        text='Товар удален!!!',
        show_alert=True
    )
    await call.message.delete()
    await call.message.answer_photo(
        caption=f'<b>🍲Название:</b> {data[1]}\n<b>💸Цена:</b> {data[2]}',
        parse_mode='HTML',
        reply_markup=inline_kb,
        photo=data[3]
    )

@router.callback_query(F.data.contains('buy_all'))
async def buy_all(call: CallbackQuery) -> None:
    data = purchases_repo.get_products(chat_id=call.from_user.id)
    total_price = 0
    
    for _, name, price, image in data:
        total_price += price
        purchases_repo.add_to_history(
            name=name,
            price=price,
            image=image,
            chat_id=call.from_user.id
        )

    purchases_repo.delete_products(chat_id=call.from_user.id)
    await call.message.delete()
    await call.message.answer(
        text=f'<b>Ваш заказ уже в пути🍲🚚</b>\n<b>💸Общая сумма: {total_price} сум</b>',
        parse_mode='HTML'
    )

@router.callback_query(F.data.contains('history_prev'))
async def get_prev_history(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')
    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)
    
    data, history_kb = get_history_kb(
        index=int(index) - 1,
        current_page=int(page) - 1,
        chat_id=call.from_user.id
    )

    media = InputMediaPhoto(media=data[2], caption=f'<b>🍲Название:</b> {data[0]}\n<b>💸Цена:</b> {data[1]} сум', parse_mode='HTML')
    await call.message.edit_media(
        media=media,
        reply_markup=history_kb
    )

@router.callback_query(F.data.contains('history_next'))
async def get_next_history(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')
    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)
    
    data, history_kb = get_history_kb(
        index=int(index) + 1,
        current_page=int(page) + 1,
        chat_id=call.from_user.id
    )

    media = InputMediaPhoto(media=data[2], caption=f'<b>🍲Название:</b> {data[0]}\n<b>💸Цена:</b> {data[1]} сум', parse_mode='HTML')
    await call.message.edit_media(
        media=media,
        reply_markup=history_kb
    )