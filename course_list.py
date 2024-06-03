from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from constants import COURSE_LIST


async def course_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    courses = user_data['courses']
    courses_text = ''
    for i, course in enumerate(courses):
        courses_text += f"\n\n{i + 1}. {course.name} {course.url}. Время обучения {', '.join(course.days)} в {course.time}."
    text = f"Твои курсы:{courses_text}"
    keyboard = [
        [InlineKeyboardButton("Редактировать", callback_data="edit"),
         InlineKeyboardButton("Удалить", callback_data="delete"),
         InlineKeyboardButton("Создать новый трекер", callback_data="create")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query

    if query is None:
        await update.message.reply_text(text=text, reply_markup=reply_markup)
    else:
        await query.answer()
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    return COURSE_LIST
