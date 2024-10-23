import os
import telebot

API_TOKEN = os.getenv('MARCIA_API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	welcome_message = 'Olá! Bem-vindo a minha farmácia!'
	bot.reply_to(message, welcome_message)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()