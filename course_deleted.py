from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from constants import COURSE_DELETED


async def course_deleted(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    courses = user_data['courses']

    course_index = int(update.message.text) - 1

    text = f"{courses[course_index].name} удалён"

    courses[course_index].job.schedule_removal()
    courses.pop(course_index)

    keyboard = [
        [InlineKeyboardButton("Создать новый трекер", callback_data="create"),
         InlineKeyboardButton("Мои курсы", callback_data="my_courses")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text=text, reply_markup=reply_markup)

    return COURSE_DELETED
