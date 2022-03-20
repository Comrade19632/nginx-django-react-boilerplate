from telegram import Update
from telegram.ext import MessageHandler, Filters, CallbackContext


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    update.message.reply_text("3212321")

def get_echo_conv_handler():
    return MessageHandler(Filters.text & ~Filters.command, echo)
