import telebot
from telebot import types
import random
import os


bot = telebot.TeleBot('5476772606:AAGVm38xU_eFZdpvlT51EYXCo_pylTPhXYo')

@bot.message_handler(content_types=['text'])

def start(message):
    if message.text.lower() == '/start':
        kbPhoto = telebot.types.ReplyKeyboardMarkup()
        kbPhoto.row('Рандомный мем')
        kbPhoto.row('Пошлый мем')
        kbPhoto.row('Политический мем')
        kbPhoto.row('Выйти')
        bot.send_message(message.from_user.id, 'Нажмите на кнопку и получите мем', reply_markup=kbPhoto)
    elif message.text.lower() == 'рандомный мем':
        photo = open('/home/lil_den/PycharmProjects/pythonProject3/mems/' + random.choice(os.listdir('/home/lil_den/PycharmProjects/pythonProject3/mems/')), 'rb')
        bot.send_photo(message.from_user.id, photo, caption='Лови')
    elif message.text.lower() == 'пошлый мем':
        photo = open('/home/lil_den/PycharmProjects/pythonProject3/mems-sex/' + random.choice(os.listdir('/home/lil_den/PycharmProjects/pythonProject3/mems-sex/')), 'rb')
        bot.send_photo(message.from_user.id, photo, caption='Держи')
    elif message.text.lower() == 'политический мем':
        photo = open('/home/lil_den/PycharmProjects/pythonProject3/Mems-polit/' + random.choice(os.listdir('/home/lil_den/PycharmProjects/pythonProject3/Mems-polit/')), 'rb')
        bot.send_photo(message.from_user.id, photo, caption='Получите')

    elif message.text.lower() == 'выйти':
        bot.send_message(message.from_user.id, 'Клавиатура убрана!!.', reply_markup=types.ReplyKeyboardRemove())


bot.polling(none_stop=True, interval=0)





