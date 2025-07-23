from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# فقط آی‌دی مجاز
ALLOWED_ID = 795698933  # آیدی عددی شما

# توکن ربات
TOKEN = 'توکن_ربات_شخصی_شما'

def start(update, context):
    if update.effective_user.id != ALLOWED_ID:
        return
    context.bot.send_message(chat_id=update.effective_chat.id, text="✅ ربات آماده است!")

updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
