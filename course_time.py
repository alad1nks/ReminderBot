from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from constants import COURSE_TIME


async def course_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    if user_data['status'] == 'create':
        course_name = update.message.text
        user_data['course_name'] = course_name
    text = ('Укажи удобное для тебя время. Например, в 9 утра ты едешь на работу в метро и у тебя есть время чтобы '
            'немного позаниматься.\n\nУказывай в 24-часовом формате: чч:мм Пример: 12:30'
            )
    keyboard = [
        [InlineKeyboardButton('Назад', callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message is None:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text=text,
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            text=text,
            reply_markup=reply_markup
        )
    return COURSE_TIME
