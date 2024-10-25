# Marcia
A pharmacy attendant BOT.

This is the base code for a Telegram Bot.
This is a very simplified version of a Bot that responds to commands sent in your Telegram chat, or echoes the message sent back to the sender.

## Observations:
* This is still just a concept test, without any commitment to supposed functionalities or real applications.
* This code is not ready to be deployed to production.
* This code doesn't do anything really useful.
* This code does not create or manage the Telegram Bot itself, the Bot must be created manually before this code is running.
* This code requires the existence of the environment variable "MARCIA_API_TOKEN" containing a valid authorization token in its execution environment.
* The token must be obtained manually on the Telegram platform.

## How to use:
1. Clone the project: 'git clone https://github.com/AndreFeitosa18/Marcia'.
2. Set the environment variable with a valid token: 'set MARCIA_API_TOKEN=xxxxxx' on Windows terminal or edit the '.bashrc' file on Unix systems.
3. Directly execute the command: 'python marcia.py' or 'python3 marcia.py' to run the code.