from telegram import Update
from telegram.ext import ContextTypes

from constants import COURSE_TIME_INVALID


async def course_time_invalid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = "Пожалуйста, введите корректное время.\n\nУказывай в 24-часовом формате: чч:мм\nПример: 12:30"

    await update.message.reply_text(text=text)
    return COURSE_TIME_INVALID
