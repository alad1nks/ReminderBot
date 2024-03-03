from telegram import Update
from telegram.ext import ContextTypes

from course_time import course_time


async def course_editing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    course_index = int(update.message.text) - 1
    user_data = context.user_data
    courses = user_data['courses']
    user_data['status'] = 'edit'
    user_data['url'] = courses[course_index].url
    user_data['name'] = courses[course_index].name

    courses[course_index].job.schedule_removal()
    courses.pop(course_index)

    return await course_time(update, context)
