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

# ============== обработчик callbacks от food_callbacks ============= #
# ==================== Завтраки ==================== #
@router.callback_query(F.data.contains('one_prev_food'))
async def get_prev_food_one(call: CallbackQuery) -> None:
    print(call.data)
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_one_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ЗАВТРАКИ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('one_next_food'))
async def get_next_food_one(call: CallbackQuery) -> None:
    print(call.data)
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_one_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ЗАВТРАКИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Горячие блюда ==================== #
@router.callback_query(F.data.contains('two_prev_food'))
async def get_prev_food_two(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_two_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ГОРЯЧИЕ БЛЮДА</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('two_next_food'))
async def get_next_food_two(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_two_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ГОРЯЧИЕ БЛЮДА</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Супы ==================== #
@router.callback_query(F.data.contains('three_prev_food'))
async def get_prev_food_three(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_three_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>СУПЫ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('three_next_food'))
async def get_next_food_three(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_three_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>СУПЫ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Салаты ==================== #
@router.callback_query(F.data.contains('four_prev_food'))
async def get_prev_food_four(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_four_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>САЛАТЫ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('four_next_food'))
async def get_next_food_four(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_four_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>САЛАТЫ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Правильное питание ==================== #
@router.callback_query(F.data.contains('five_prev_food'))
async def get_prev_food_five(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_five_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ПРАВИЛЬНОЕ ПИТАНИЕ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('five_next_food'))
async def get_next_food_five(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_five_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ПРАВИЛЬНОЕ ПИТАНИЕ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Сэндвичи ==================== #
@router.callback_query(F.data.contains('six_prev_food'))
async def get_prev_food_six(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_six_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>СЭНДВИЧИ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('six_next_food'))
async def get_next_food_six(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_six_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>СЭНДВИЧИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(
        media=media,
        reply_markup=get_one_kb
    )
# ================================================== #

# ==================== Паста ==================== #
@router.callback_query(F.data.contains('seven_prev_food'))
async def get_prev_food_seven(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_seven_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ПАСТА</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('seven_next_food'))
async def get_next_food_seven(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_seven_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ПАСТА</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Гарниры ==================== #
@router.callback_query(F.data.contains('eight_prev_food'))
async def get_prev_food_eight(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_eight_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ГАРНИРЫ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(
        media=media,
        reply_markup=get_one_kb
    )

@router.callback_query(F.data.contains('eight_next_food'))
async def get_next_food_eight(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_eight_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ГАРНИРЫ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Блины ==================== #
@router.callback_query(F.data.contains('nine_prev_food'))
async def get_prev_food_nine(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_nine_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>БЛИНЫ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('nine_next_food'))
async def get_next_food_nine(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_nine_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>БЛИНЫ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Вафли ==================== #
@router.callback_query(F.data.contains('ten_prev_food'))
async def get_prev_food_ten(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_ten_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ВАФЛИ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('ten_next_food'))
async def get_next_food_ten(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_ten_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ВАФЛИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Хлеб ==================== #
@router.callback_query(F.data.contains('eleven_prev_food'))
async def get_prev_food_eleven(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_eleven_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ХЛЕБ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('eleven_next_food'))
async def get_next_food_eleven(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_eleven_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ХЛЕБ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Кофе ==================== #
@router.callback_query(F.data.contains('twelve_prev_food'))
async def get_prev_food_twelve(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_twelve_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>КОФЕ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('twelve_next_food'))
async def get_next_food_twelve(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_twelve_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>КОФЕ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Чай ==================== #
@router.callback_query(F.data.contains('thirteen_prev_food'))
async def get_prev_food_thirteen(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_thirteen_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ЧАЙ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('thirteen_next_food'))
async def get_next_food_thirteen(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_thirteen_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ЧАЙ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Фреши ==================== #
@router.callback_query(F.data.contains('fourteen_prev_food'))
async def get_prev_food_fourteen(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_fourteen_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>ФРЕШИ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('fourteen_next_food'))
async def get_next_food_fourteen(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_fourteen_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>ФРЕШИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #

# ==================== Напитки ==================== #
@router.callback_query(F.data.contains('fifteen_prev_food'))
async def get_prev_food_fifteen(call: CallbackQuery) -> None:
    _, index, page = call.data.split(':')

    if int(page) == 1:
        return await call.answer(text='Первая страница', show_alert=True)

    data, get_one_kb = get_fifteen_category_kb(index=int(index) - 1, current_page=int(page) - 1)
    image = data['image']

    text = f'<b>НАПИТКИ</b>\n\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)

@router.callback_query(F.data.contains('fifteen_next_food'))
async def get_next_food_fifteen(call: CallbackQuery) -> None:
    _, index, page, total_pages = call.data.split(':')

    if int(page) == int(total_pages):
        return await call.answer(text='Последняя страница', show_alert=True)

    data, get_one_kb = get_fifteen_category_kb(index=int(index) + 1, current_page=int(page) + 1)

    image = data['image']

    text = f'<b>НАПИТКИ</b>\n\n<b>🍲Название:</b> {data['name']}\n<b>🧾Описание:</b> {data['description']}\n\n<b>💸Цена:</b> {data['price']} сум'
    media = InputMediaPhoto(media=image, caption=text, parse_mode='HTML')
    await call.message.edit_media(media=media, reply_markup=get_one_kb)
# ================================================== #