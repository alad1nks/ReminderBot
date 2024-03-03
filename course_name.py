from telegram import Update
from telegram.ext import ContextTypes

from constants import COURSE_NAME


async def course_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    url = update.message.text
    user_data = context.user_data
    user_data["course_url"] = url
    text = "Как называется твой курс?"
    await update.message.reply_text(text=text)
    return COURSE_NAME
