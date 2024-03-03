from telegram import Update
from telegram.ext import ContextTypes

from constants import COURSE_LINK_INVALID


async def course_link_invalid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = "Пожалуйста, введите корректную ссылку на курс"

    await update.message.reply_text(text=text)
    return COURSE_LINK_INVALID
