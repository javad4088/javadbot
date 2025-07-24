import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")
USER_ID = os.environ.get("AUTHORIZED_USER_ID")

def start(update, context):
    if str(update.effective_user.id) != str(USER_ID):
        return
    update.message.reply_text("✅ ربات متصل شد!")

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
