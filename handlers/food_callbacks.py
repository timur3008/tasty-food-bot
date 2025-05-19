from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InputMediaPhoto

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

@router.callback_query(F.data == 'Завтраки')
async def get_one_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_one_category_kb()

    text = f'<b>ЗАВТРАКИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Горячие блюда')
async def get_two_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_two_category_kb()

    text = f'<b>ГОРЯЧИЕ БЛЮДА</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Супы')
async def get_three_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_three_category_kb()

    text = f'<b>СУПЫ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Салаты')
async def get_four_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_four_category_kb()

    text = f'<b>САЛАТЫ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Правильное питание')
async def get_five_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_five_category_kb()

    text = f'<b>ПРАВИЛЬНОЕ ПИТАНИЕ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Сэндвичи')
async def get_six_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_six_category_kb()

    text = f'<b>СЭНДВИЧИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Паста')
async def get_seven_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_seven_category_kb()

    text = f'<b>ПАСТА</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Гарниры')
async def get_eight_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_eight_category_kb()

    text = f'<b>ГАРНИРЫ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Блины')
async def get_nine_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_nine_category_kb()

    text = f'<b>БЛИНЫ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Вафли')
async def get_ten_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_ten_category_kb()

    text = f'<b>ВАФЛИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Хлеб')
async def get_eleven_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_eleven_category_kb()

    text = f'<b>ХЛЕБ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Кофе')
async def get_twelve_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_twelve_category_kb()

    text = f'<b>КОФЕ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Чай')
async def get_thirteen_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_thirteen_category_kb()

    text = f'<b>ЧАЙ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Фреши')
async def get_fourteen_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_fourteen_category_kb()

    text = f'<b>ФРЕШИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

@router.callback_query(F.data == 'Напитки')
async def get_fifteen_category(call: CallbackQuery) -> None:
    await call.message.delete()
    data, get_keyboard = get_fifteen_category_kb()

    text = f'<b>НАПИТКИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    image = data['image']

    await call.message.answer_photo(photo=image, caption=text, parse_mode='HTML', reply_markup=get_keyboard)

# ============ Обработка callbacks получаемых от кнопок в Корзине ================ #
@router.callback_query(F.data.contains('purchase_prev'))
async def get_purchase_prev(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)
    
    data, inline_kb = get_purchases_kb(index=int(index) - 1, current_page=int(page) - 1, chat_id=call.from_user.id)
    media = InputMediaPhoto(media=data[3], caption=f'<b>🍲Название:</b> {data[1]}\n<b>💸Цена:</b> {data[2]} сум', parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=inline_kb)

@router.callback_query(F.data.contains('purchase_next'))
async def get_purchase_next(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)
    
    data, inline_kb = get_purchases_kb(index=int(index) + 1, current_page=int(page) + 1, chat_id=call.from_user.id)
    media = InputMediaPhoto(media=data[3], caption=f'<b>🍲Название:</b> {data[1]}\n<b>💸Цена:</b> {data[2]} сум', parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=inline_kb)
# ================================================================================ #