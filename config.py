__all__ = [
	'API_TOKEN',
	'PHARMACY_CATEGORIES',
	'MAIN_MENU_COMMANDS'
]

import os


# Load the environment variable with the authorization token to connect the API:
API_TOKEN = os.getenv('MARCIA_API_TOKEN')


# A list of pharmaceutical product categories, shown with the '/CATEGORIES' command:
PHARMACY_CATEGORIES = [
	'/PAINKILLERS - From all brands, to relieve your pain',
	'/ANTIBIOTICS - The best and most effective antibiotics on the market'
]


# The list of main menu commands, shown with the '/HELP' command:
MAIN_MENU_COMMANDS = [
	'/START - Show introductory message',
	'/CATEGORIES - Show pharmacy categories',
	'/HELP - Show this help message',
	'* You can use uppercase or lowercase letters in the command.'
]