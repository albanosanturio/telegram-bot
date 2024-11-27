from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


token_path = "token.txt"
with open(token_path) as file:
        token = file.read()

print(token)

BOT_USERNAME = "@argentinian_quotes_bot"

#asyn makes functions asyncronous
#async def