
from telegram import *
from telegram.ext import *

api_key = "5170347007:AAHRLYqkz0qvOdS0NzwE5JDdgdF1mRr55RE"
bot = Bot(api_key)
# print(bot.get_me())        --> to get values of our bot (or to check)
updater = Updater(api_key, use_context=True)
disp = updater.dispatcher


def check1(update, context):
    update.message.reply_text("bhosidi wala")


def handleplz(update, context):
    update.message.reply_text(
        "is it working   ")


def error(update, context):
    update.message.reply_text("ooops! there is an error")


disp.add_handler(CommandHandler("verma", check1))
disp.add_handler(MessageHandler(Filters.text, handleplz))
disp.add_error_handler(error)

updater.start_polling()
updater.idle()
