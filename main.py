from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇺🇸 Welcome to USA Trucking Dispatch AI Bot!\n\n"
        "Use these commands:\n"
        "/driver - Driver Registration\n"
        "/owner - Owner Operator\n"
        "/load - Post Load\n"
        "/truck - Truck Available\n"
        "/job - Dispatch Jobs\n"
        "/help - Help"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Need help? Contact the group admin."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

print("Bot Started...")
app.run_polling()
