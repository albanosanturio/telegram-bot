from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


token_path = "token.txt"
with open(token_path) as file:
        token = file.read()

print(token)

BOT_USERNAME = "@argentinian_quotes_bot"


#COMMANDS
#asyn makes functions asyncronous
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a bot beep beep boludo")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom command')


# RESPONSES

def handle_response(text: str) -> str:
    processed_text: str = text.lower()
    if "hello" in processed_text:
         return "Hey there"
    if "how are you" in processed_text:
         return "all gooood"
    if "aguante argentina" in processed_text:
         return "sapee"
    return "EHHHH?"


#Messages

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
               new_text: str = text.replace(BOT_USERNAME, '').strip()
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'User {update} caused error {context.error}')


if __name__ == '__main__':
     print('starting bot')
     app = Application.builder().token(token).build()
     
     #Commands
     app.add_handler(CommandHandler('start', start_command))
     app.add_handler(CommandHandler('help', help_command))
     app.add_handler(CommandHandler('custom', custom_command))

     # Messages
     app.add_handler(MessageHandler(filters.TEXT, handle_message))

     #Errors
     app.add_error_handler(error)

     # Polls the bot
     print("Polling...")
     app.run_polling(poll_interval=3)
      
     
