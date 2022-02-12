from telegram import *
from telegram.ext import *
import os
api_key = "5170347007:AAHRLYqkz0qvOdS0NzwE5JDdgdF1mRr55RE"


def check1(update, context):
    update.message.reply_text(
        "this is a automated message to you and i have created using heroku app")


def handleplz(update, context):
    if(update.message.text == "abhishek"):
        update.message.reply_text("is a vhutiya londa")


def error(update, context):
    update.message.reply_text("ooops! there is an error")


def main():
    updater = Updater(api_key, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(CommandHandler("verma", check1))
    disp.add_handler(MessageHandler(Filters.text, handleplz))
    disp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=os.environ.get(
        "PORT", 443), url_path=api_key, webhook_url="https://deltaxpr.herokuapp.com/"+api_key)
    updater.idle()


if __name__ == "__main__":
    main()
