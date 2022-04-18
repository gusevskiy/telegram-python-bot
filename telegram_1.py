# telegram-python-bot
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler


TOKEN = '5327970335:AAGrQuz_BnxBUz8G5ZWtSh2ViirtesamX6Q'

def message_hadler(update: Update, context: CallbackContext):
    return update.message.reply_text(text='Ура работает!')

def main():
    updater = Updater(
        token=TOKEN,
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_hadler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


