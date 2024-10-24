from telebot import TeleBot
from telebot.types import Message

from config import PHARMACY_CATEGORIES, MAIN_MENU_COMMANDS


class MainMenu:
	""" The BOT main menu class """
	def register_response_methods(self, bot: TeleBot) -> None:
		""" The method that records response methods associated with commands """
		# Decorates the response function to the '/CATEGORIES' command:
		@bot.message_handler(func=lambda message: '/CATEGORIES' == message.text.upper())
		def categories_command(message: Message) -> None:
			bot.reply_to(message, str(PHARMACY_CATEGORIES).strip("[']").replace("', '", ".\r\n"))
		# Decorates the response function to the '/HELP' command:
		@bot.message_handler(func=lambda message: '/HELP' == message.text.upper())
		def help_command(message: Message) -> None:
			bot.reply_to(message, str(MAIN_MENU_COMMANDS).strip("[']").replace("', '", ".\r\n"))