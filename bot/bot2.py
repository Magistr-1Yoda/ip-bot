import telebot
import main
from telebot import *
bot = telebot.TeleBot("6279309417:AAE88A0P3Pc8F-dw9BLiMYXqsj5pprTyP6w")

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.username
    user_id = message.from_user.id
    if db.check_user(user_id):
        bot.send_message(message.chat.id, 'Добро пожаловать!')
    else:
        db.register(user_id, name)
        bot.send_message(message.chat.id, 'Спасибо за регистрацию!')
    

@bot.message_handler(func= lambda m : m.text)
def pay(message):
    markup = types.InlineKeyboardMarkup()
    btn1 =  types.InlineKeyboardButton('Посмотреть товары', callback_data = "tovar")
    btn2 = types.InlineKeyboardButton('Пополнить баланс', callback_data = "balance")
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Это магазин и тд и тп(описание магазина)', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call, user_id):
    if call.data == "tovar":
        markup = types.InlineKeyboardMarkup()
        btn1 =  types.InlineKeyboardButton('Курсы по Python', callback_data = "Python")
        btn2 =  types.InlineKeyboardButton('Курсы по С#', callback_data = "C#")
        btn3 =  types.InlineKeyboardButton('Курсы по С++', callback_data = "C++")
        btn4 = types.InlineKeyboardButton('Главное меню', callback_data = "menu")
        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,  message_id=call.message.message_id,  reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def money(call, user_id):
    if call.data == "balance":
        thousand = 1000
        db.update_balance(user_id, thousand, True)
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Главное меню', callback_data = "menu")
        markup.add(btn1)

def Python(call):
    pass


        


def menu(call):
    if call.data == 'menu':
        pay()

if __name__ == '__main__':
    db = main.Database()
    bot.infinity_polling()