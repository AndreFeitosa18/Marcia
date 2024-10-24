from telebot import TeleBot
from telebot.types import Message


class MainMenu:
	""" The BOT main menu class """
	def register_response_methods(self, bot: TeleBot) -> None:
		""" The method that records response methods associated with commands """
		# Decorates the response function to the '/help' command:
		@bot.message_handler(commands=['help'])
		def help_command(message: Message) -> None:
			bot.reply_to(message, 'Comando /help')