from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from constants import REMIND_MESSAGE


async def remind_message(context: CallbackContext) -> int:
    job_data = context.job.data

    chat_id = job_data['chat_id']
    course_name = job_data['course_name']
    course_url = job_data['course_url']

    text = f"Пора учиться! Твой курс {course_name}\n\n{course_url}"

    keyboard = [
        [InlineKeyboardButton("Создать новый трекер", callback_data="remind_message_create"),
         InlineKeyboardButton("Мои курсы", callback_data="remind_message_my_courses")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=reply_markup
    )

    return REMIND_MESSAGE
