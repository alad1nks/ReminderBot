from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from constants import EDIT_COURSE


async def edit_course(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = "Введи порядковый номер курса из сообщения выше"
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data="back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=reply_markup
    )

    return EDIT_COURSE
