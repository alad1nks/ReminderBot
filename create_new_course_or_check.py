import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from constants import CREATE_NEW_COURSE_OR_CHECK, moscow_tz
from course import Course
from remind_message import remind_message


async def create_new_course_or_check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    chat_id = update.effective_chat.id

    course_name = user_data['course_name']
    course_url = user_data['course_url']
    course_days = user_data['course_days']
    course_time = user_data['course_time']
    selected_options = user_data['selected_options']

    hour, minute = map(int, course_time.split(':'))
    time = datetime.time(hour=hour, minute=minute, tzinfo=moscow_tz)

    job = context.job_queue.run_daily(
        remind_message,
        time=time,
        days=map(int, selected_options),
        data={'chat_id': chat_id, 'course_name': course_name, 'course_url': course_url}
    )

    new_course = Course(course_name, course_url, course_days, course_time, job)

    courses = user_data['courses']
    courses.append(new_course)

    text = "Отлично! Мы обязательно пришлём тебе напоминание в указанное время.\n\nПродуктивного дня 🍎"

    keyboard = [
        [InlineKeyboardButton("Создать новый трекер", callback_data="create"),
         InlineKeyboardButton("Мои курсы", callback_data="my_courses")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=text,
        reply_markup=reply_markup
    )

    return CREATE_NEW_COURSE_OR_CHECK
