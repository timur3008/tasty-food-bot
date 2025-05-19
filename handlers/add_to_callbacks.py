from typing import Any
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InputMediaPhoto

from database.database import purchases_repo

from keyboards.inline import (
    get_one_category_kb,
    get_two_category_kb,
    get_three_category_kb,
    get_four_category_kb,
    get_five_category_kb,
    get_six_category_kb,
    get_seven_category_kb,
    get_eight_category_kb,
    get_nine_category_kb,
    get_ten_category_kb,
    get_eleven_category_kb,
    get_twelve_category_kb,
    get_thirteen_category_kb,
    get_fourteen_category_kb,
    get_fifteen_category_kb,
    get_purchases_kb
)

router = Router()

# отлавливаем callbacks c Добавить в корзину
@router.callback_query(F.data.contains('add_to_one'))
async def add_to_one_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_one_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅',show_alert=True)

@router.callback_query(F.data.contains('add_to_two'))
async def add_to_two_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_two_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_three'))
async def add_to_three_basket(call: CallbackQuery) -> None:
    _, index = call.data.split(':')
    data, _ = get_three_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_four'))
async def add_to_four_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_four_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_five'))
async def add_to_five_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_five_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_six'))
async def add_to_six_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_six_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_seven'))
async def add_to_seven_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_seven_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_eight'))
async def add_to_eight_basket(call: CallbackQuery) -> None:
    _, index = call.data.split(':')
    data, _ = get_eight_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_nine'))
async def add_to_nine_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_nine_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_ten'))
async def add_to_ten_basket(call: CallbackQuery) -> None:
    _, index = call.data.split(':')
    data, _ = get_ten_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_eleven'))
async def add_to_eleven_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_eleven_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_twelve'))
async def add_to_twelve_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_twelve_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id
    )
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_thirteen'))
async def add_to_thirteen_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_thirteen_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_fourteen'))
async def add_to_fourteen_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_fourteen_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)

@router.callback_query(F.data.contains('add_to_fiveteen'))
async def add_to_fiveteen_basket(call: CallbackQuery) -> Any:
    _, index = call.data.split(':')
    data, _ = get_fifteen_category_kb(index=int(index))
    
    purchases_repo.add_product(name=data['name'], price=int(data['price']), image=data['image'], chat_id=call.from_user.id)
    
    return await call.answer(
        text=f'"{data['name']}" успешно добавлена в корзину✅', show_alert=True)