import json
from typing import Any

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.products import products
from database.database import purchases_repo

total_pages = len(products) // 5

def categories_keyboard(start: int = 0, finish: int = 5, current_page: int = 1) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    for category_name in list(products.keys())[start:finish]:
        keyboard.button(text=category_name, callback_data=category_name)

    keyboard.adjust(1)

    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'prev:{start}:{finish}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'next:{start}:{finish}:{current_page}:{total_pages}')
    )
    return keyboard.as_markup()

def get_one_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Завтраки'])

    data = products['Завтраки'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'one_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'one_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text="Добавить в корзину", callback_data=f'add_to_one:{index}')
    )
    return data, keyboard.as_markup()

def get_two_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Горячие блюда'])

    data = products['Горячие блюда'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'two_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'two_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_two:{index}')
    )
    return data, keyboard.as_markup()

def get_three_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Супы'])

    data = products['Супы'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'three_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'three_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_three:{index}')
    )
    return data, keyboard.as_markup()

def get_four_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Салаты'])

    data = products['Салаты'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'four_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'four_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_four:{index}')
    )
    return data, keyboard.as_markup()

def get_five_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Правильное питание'])

    data = products['Правильное питание'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'five_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'five_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_five:{index}')
    )
    return data, keyboard.as_markup()

def get_six_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Сэндвичи'])

    data = products['Сэндвичи'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'six_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'six_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_six:{index}')
    )
    return data, keyboard.as_markup()

def get_seven_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Паста'])

    data = products['Паста'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'seven_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'seven_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_seven:{index}')
    )
    return data, keyboard.as_markup()

def get_eight_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Гарниры'])

    data = products['Гарниры'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'eight_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'eight_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_eight:{index}')
    )
    return data, keyboard.as_markup()

def get_nine_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Блины'])

    data = products['Блины'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'nine_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'nine_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_nine:{index}')
    )
    return data, keyboard.as_markup()

def get_ten_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Вафли'])

    data = products['Вафли'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'ten_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'ten_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_ten:{index}')
    )
    return data, keyboard.as_markup()

def get_eleven_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Хлеб'])

    data = products['Хлеб'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'eleven_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'eleven_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_eleven:{index}')
    )
    return data, keyboard.as_markup()

def get_twelve_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Кофе'])

    data = products['Кофе'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'twelve_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'twelve_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_twelve:{index}')
    )
    return data, keyboard.as_markup()

def get_thirteen_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Чай'])

    data = products['Чай'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'thirteen_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'thirteen_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_thirteen:{index}')
    )
    return data, keyboard.as_markup()

def get_fourteen_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Фреши'])

    data = products['Фреши'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'fourteen_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'fourteen_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_fourteen:{index}')
    )
    return data, keyboard.as_markup()

def get_fifteen_category_kb(index: int = 0, current_page: int = 1) -> tuple[Any, InlineKeyboardMarkup]:
    keyboard = InlineKeyboardBuilder()
    total_pages = len(products['Напитки'])

    data = products['Напитки'][index]
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'fiveteen_prev_food:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'fiveteen_next_food:{index}:{current_page}:{total_pages}')
    )
    keyboard.row(
        InlineKeyboardButton(text='На главную', callback_data='home'),
        InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_to_fiveteen:{index}')
    )
    return data, keyboard.as_markup()

def get_purchases_kb(index: int = 0, current_page: int = 1, chat_id: int = None) -> tuple | None:
    keyboard = InlineKeyboardBuilder()

    if len(purchases_repo.get_products(chat_id=chat_id)) == 0:
        return None, None

    data = purchases_repo.get_products(chat_id=chat_id)[index]
    
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'purchase_prev:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{len(purchases_repo.get_products(chat_id=chat_id))}', callback_data=f'current'),
        InlineKeyboardButton(text='>>>', callback_data=f'purchase_next:{index}:{current_page}:{len(purchases_repo.get_products(chat_id=chat_id))}')
    )
    keyboard.row(
        InlineKeyboardButton(text='Удалить с корзины', callback_data=f'del_from_bask:{data[0]}'),
        InlineKeyboardButton(text='Заказать всё', callback_data=f'buy_all')
    )
    return data, keyboard.as_markup()

def get_history_kb(index: int = 0, current_page: int = 1, chat_id: int = None) -> tuple | None:
    keyboard = InlineKeyboardBuilder()

    if len(purchases_repo.get_history(chat_id=chat_id)) == 0:
        return None, None
    
    total_pages = len(purchases_repo.get_history(chat_id=chat_id))
    data = purchases_repo.get_history(chat_id=chat_id)[index]
    
    keyboard.row(
        InlineKeyboardButton(text='<<<', callback_data=f'history_prev:{index}:{current_page}'),
        InlineKeyboardButton(text=f'{current_page}:{total_pages}', callback_data='current_history'),
        InlineKeyboardButton(text='>>>', callback_data=f'history_next:{index}:{current_page}:{total_pages}')
    )

    return data, keyboard.as_markup()