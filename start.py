from telegram import Update
from telegram.ext import ContextTypes

from constants import COURSE_LINK

text = (
    "Привет! Мы здесь чтобы помочь тебе погрузиться в микро-обучение. Ты можешь использовать нашего бота, чтобы "
    "отслеживать свой прогресс и не забывать проходить обучение 📚  Для этого пришли ссылку на твой курс"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    user_data['courses'] = []
    user_data['status'] = 'create'
    await update.message.reply_text(text=text)
    return COURSE_LINK


async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    user_data['status'] = 'create'
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=text)
    return COURSE_LINK
