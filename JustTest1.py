import telebot
import random
import datetime
from datetime import datetime
from pytz import timezone

bot = telebot.TeleBot('1019968029:AAEdaVL7zgsYihvbMcr4bCeL3hrZqrjM3MM')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Стартуй нахуй!')
    bot.send_message(message.chat.id, datetime.now(timezone('Europe/Moscow')))



bot.polling(none_stop=True, interval=0)
