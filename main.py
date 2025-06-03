from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# دستور start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("السلام علیکم! خوش آمدی به ربات لحافظون 🌿\nقرائتت را بفرست تا بررسی کنیم.")

# دستور help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - آغاز کار\n/recite - ارسال قرائت\n/about - درباره ما")

# دستور about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات لحافظون ساخته شده برای کمک به حافظان قرآن کریم در تصحیح قرائت.\n🕌 طراحی‌شده توسط یک معلم مؤمن و خلاق.")

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("about", about))

    app.run_polling()
