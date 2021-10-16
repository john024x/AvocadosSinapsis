import logging
from telegram.ext import *
import responses
API_KEY = '2080829219:AAHE54vdqtkXboN3BBE30RT2jz1ks7ktIMo'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hola buenas 😎')


def help_command(update, context):
    update.message.reply_text('Si necesitas mas ayuda puedes visitar google.com! seguro encuentras tu respuesta')


def custom_command(update, context):
    update.message.reply_text('Este comando era secreto, como lo descubriste???')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'El usuario ({update.message.chat.id}) dijo: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Se provoco un error {update} causando {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()