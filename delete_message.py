from telegram import Update
from telegram.ext import ContextTypes


async def delete_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()
    await query.delete_message()
