from telebot import telebot
from telebot.types import KeyboardButton,ReplyKeyboardMarkup
import sqlite3

TOKEN='5941445137:AAEfka6_Ob4IIi9jT80v_GPWxgWhPUCVOYg'

bot=TeleBot(TOKEN,parse_mode=None)

def main_menu_keyboard():

    """
    Эта функция создает первоначальное иеню в нашем телеграм боте.

    :return Объект класса ReplyKeyboardMarkup
    """

    cart=KeyboardButton("Корзина")
    menu=KeyboardButton("Меню")

    keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(menu)
    keyboard.add(cart)

    return keyboard


def get_product_names()->list:
    products=[]


    try:
        conn=sqlite3.connect("pizza_databse.db")
        cursor=conn.cursor()

    except Exception as e:
        print(e)






def menu_keyboard():
    """
    Это меню высвечивает товары в нашей базе данных

    :return:Объект класса ReplyKeyboardMarkup
    """

    products=get_product_names()

    row=[]
    for product in products:
        button = KeyboardButton(button)
        row.append(button)

        if len(row)==2
            keboard.add(row)
            row=[]
    if row:
        keyboard.add(row)
    back_button=KeyboardButton("<<Назад")

    keyboard.add(back_button)

    return keyboard


@bot.message_handler(commands=['start'])
def start_handler(message)

