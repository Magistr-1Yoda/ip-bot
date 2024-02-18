import telebot
from telebot import types
import alhimi

bot = telebot.TeleBot('6279309417:AAE88A0P3Pc8F-dw9BLiMYXqsj5pprTyP6w')

start_keyboard = {
    '🛒 Магазин' : 'shop',
    '💳  Пополнить баланс' : 'balance',
    '🛠️ Админка' : 'admin',
}

def inline_keyboards_create(dictionary : dict, NumberColumns=1):
    keyboards = types.InlineKeyboardMarkup(row_width=NumberColumns)
    btn_names = [types.InlineKeyboardButton(text=key, callback_data=value) for key, value in dictionary.items()]
    keyboards.add(*btn_names)
    return keyboards

@bot.message_handler(commands=['start'])
def start(message):   
    user_id = message.from_user.id
    if db.get_user(user_id):
        bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=inline_keyboards_create(start_keyboard))
    else:
        db.register(str(user_id), message.from_user.username)
        bot.send_message(message.chat.id, 'Спасибо за регистрацию, Добро пожаловать!', reply_markup=inline_keyboards_create(start_keyboard))

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    callback_data = call.data
    if callback_data == 'balance':
        balance_get(call)
    elif callback_data == 'admin':
        admin_get(call)
    elif callback_data == 'add_product':
        product_get(call)
    elif callback_data == 'shop':
        shop(call)

def shop(call):
    products = db.get_all_products()
    if products:
        product_dict = {f'{product.name} - {product.price} ₽': product.id for product in products}
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Список товаров:", reply_markup=inline_keyboards_create(product_dict))
    else:
        bot.send_message(chat_id=call.message.chat.id,
                         text="В базе данных нет товаров.")

def balance_get(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        text="На какую сумму вы хотите пополнить баланс?")    
    bot.register_next_step_handler(msg, update_bln)
    

def update_bln(message):
    balance = message.text
    user_id = message.from_user.id
    result = db.update_balance(user_id, balance, True)
    bot.send_message(message.chat.id, f"Ваш баланс пополнен на {balance}, теперь у вас {result}", reply_markup=inline_keyboards_create(start_keyboard))

def admin_get(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=("Введите пароль, что бы войти в админку"))
    bot.register_next_step_handler(msg, password)
def password(call):
    password = call.message.text
    if password == 123456:
        bot.send_message(chat_id=call.message.chat.id, 
                        text="Выберите действие:", 
                        reply_markup=inline_keyboards_create({'Добавить товар': 'add_product'}))
    #else:
     #  bot.send_message(chat_id=call.message.chat.id, text=("Вы вели пароль не правильно!"), reply_markup=inline_keyboards_create(start_keyboard))
            
def product_get(call):
    bot.send_message(chat_id=call.message.chat.id, 
                     text="Введите название товара:", 
                     reply_markup=inline_keyboards_create(start_keyboard))
    bot.register_next_step_handler(call.message, name_product)

def name_product(message):
    name = message.text
    bot.send_message(chat_id=message.chat.id, text="Введите цену товара:")
    bot.register_next_step_handler(message, price_product, name)

def price_product(message, name):
    price = message.text
    db.add_product(name=name, price=price)
    bot.send_message(chat_id=message.chat.id, text="Успешно добавлено!", reply_markup=inline_keyboards_create(start_keyboard))


if __name__ == '__main__':
    db = alhimi.Database()
    bot.infinity_polling()