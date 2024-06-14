from config import token

import telebot
from random import choice


bot = telebot.TeleBot(token)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
здарова\
""")

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text) 

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()