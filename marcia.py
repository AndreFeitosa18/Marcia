from telebot import ExceptionHandler, TeleBot
from telebot.handler_backends import HandlerBackend
from telebot.storage import StateMemoryStorage, StateStorageBase
from telebot.types import Message

import config
from menu.main import MainMenu


class Marcia(TeleBot):
	""" The BOT class Marcia, a pharmacy attendant """
	def __init__(self, token: str, parse_mode: config.API_TOKEN = None, threaded: bool | None = True, skip_pending: bool | None = False, num_threads: int | None = 2, next_step_backend: HandlerBackend | None = None, reply_backend: HandlerBackend | None = None, exception_handler: ExceptionHandler | None = None, last_update_id: int | None = 0, suppress_middleware_excepions: bool | None = False, state_storage: StateStorageBase | None = ..., use_class_middlewares: bool | None = False, disable_web_page_preview: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_sending_without_reply: bool | None = None, colorful_logs: bool | None = False, validate_token: bool | None = True):
		""" Initializes the Marcia class with the same parameters as the TeleBot class. (These parameters are passed to the superclass) """
		super().__init__(token, parse_mode, threaded, skip_pending, num_threads, next_step_backend, reply_backend, exception_handler, last_update_id, suppress_middleware_excepions, state_storage, use_class_middlewares, disable_web_page_preview, disable_notification, protect_content, allow_sending_without_reply, colorful_logs, validate_token)
		# Decorates the response function to the '/start' command:
		@self.message_handler(commands=['start'])
		def start_command(message: Message) -> None:
			self.reply_to(message, 'Comando /start')
		# Register main menu response methods:
		MainMenu().register_response_methods(self)
		# Decorates the function that echoes sent messages:
		@self.message_handler(func=lambda message: True)
		def echo_message(message: Message) -> None:
			self.reply_to(message, message.text)


if __name__ == '__main__':
	Marcia(config.API_TOKEN).infinity_polling()