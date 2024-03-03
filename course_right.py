from telegram import InlineKeyboardButton, Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from constants import COURSE_RIGHT, days


async def course_right(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    course_name = user_data['course_name']
    course_days = user_data['course_days']
    course_time = user_data['course_time']
    selected_options = user_data['selected_options']
    for option in sorted(selected_options):
        course_days.append(days[option])
    text = f"Итак, курс {course_name}. Время обучения {', '.join(course_days)} в {course_time}.\n\nВсё верно?"
    keyboard = [
        [InlineKeyboardButton('Да', callback_data='yes'), InlineKeyboardButton('Назад', callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=text,
        reply_markup=reply_markup
    )

    return COURSE_RIGHT
