from telegram import Update
from telegram.ext import ContextTypes

from advertisement_message import advertisement_message
from constants import COURSE_LINK

text = (
    "Привет! Мы здесь чтобы помочь тебе погрузиться в микро-обучение. Ты можешь использовать нашего бота, чтобы "
    "отслеживать свой прогресс и не забывать проходить обучение 📚  Для этого пришли ссылку на твой курс"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data

    if 'courses' not in user_data:
        user_data['courses'] = []

        chat_id = update.effective_chat.id
        context.job_queue.run_once(
            advertisement_message,
            when=5,
            data={'chat_id': chat_id}
        )

    user_data['status'] = 'create'

    query = update.callback_query

    if query is None:
        await update.message.reply_text(text=text)
    else:
        await query.answer()
        await query.edit_message_text(text=text)

    return COURSE_LINK
