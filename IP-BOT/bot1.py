import telebot
import random
from telebot import *

bot = telebot.TeleBot("")

list_anegtot = ["Встретились как-то раз мимоза, тюльпан и роза. И начался у них спор, кто из них самый красивый.", 
                "Собрались однажды марсианин, инопланетянин и человек. И поспорили, чья планета лучше.",
                "Пошли как-то в лес медведь, заяц и лиса. И решили они выяснить, кто из них быстрее.",
                "Собрались на берегу реки слон, бегемот и крокодил. И начали они спорить, кто из них сильнее.",
                "Решили как-то мышь, кот и собака устроить соревнование, кто из них лучше ловит птиц.",
                "Поспорили как-то компьютер, калькулятор и смартфон, кто из них умнее.",
                "Собрались в пустыне верблюд, скорпион и варан. И стали они обсуждать, кто из их более выносливый.",
                "Поспорили однажды яйцо, цыпленок и курица, кто из них главнее.",
                "Собрались вместе автомобиль, велосипед и самокат. И затеяли они спор, кто из них наиболее удобный."]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 =  types.InlineKeyboardButton('Информация о боте', callback_data = "Info")
    markup.add(btn1, )
    bot.send_message(message.chat.id, 'Всем привет, это главное меню!', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "Info":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Начать👍", callback_data = "Go"))
        bot.send_message(call.message.chat.id, "Этот бот поможет вам посмеяться и улыбнуться, здесь вы сможете прочитать много интересных и смешных анекдотов ", reply_markup=markup)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,  message_id=call.message.message_id,  reply_markup=markup)
    elif call.data == "Go":
        markup = types.ReplyKeyboardMarkup()
        btn1 = "Простой анекдот"
        btn2 = "С черным юмором"
        btn3 = "Детский анекдот"
        markup.add(btn1,btn2,btn3)
        bot.send_message(call.message.chat.id, "Выберите какой анекдот вы хотите")
@bot.message_handler(func= lambda m : m.text)







if __name__ == '__main__':
    bot.infinity_polling()


