from asyncore import dispatcher
from os import enviro
from tracemalloc import start

from telegram import *
from telegram.ext import *

api_key = "5170347007:AAHRLYqkz0qvOdS0NzwE5JDdgdF1mRr55RE"
bot = Bot(api_key)
# print(bot.get_me())        --> to get values of our bot (or to check)


def check1(update, context):
    update.message.reply_text("hey")


def error(update, context):
    update.message.reply_text("error enchontered")


def handleplz(update, context):
    update.message.reply_text(
        "hello messager i will be called everytime you message in thsi group  ")


def main():
    updater = Updater(api_key, use_context=True)
    disp = updater.dispatcher
    disp.add_handler(CommandHandler("verma", check1))
    disp.add_handler(MessageHandler(Filters.text, handleplz))
    disp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=os.environ.get(
        "PORT", 443), webhook_url="https://deltaxpr.herokuapp.com/"+api_key)
    updater.idle()


if __name__ == '__main__':
    main()
