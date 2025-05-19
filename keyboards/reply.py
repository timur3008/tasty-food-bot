from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

def start_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text='Меню')
    keyboard.button(text='Корзина')
    keyboard.button(text='История заказов')

    keyboard.adjust(2, 1)
    return keyboard.as_markup(resize_keyboard=True)