from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, ContextTypes

from constants import ADVERTISEMENT_MESSAGE


async def advertisement_message(context: CallbackContext) -> int:
    job_data = context.job.data

    chat_id = job_data['chat_id']

    text = (f"Хочешь купить удобный шаблон, который поможет ещё более эффективно планировать задачи?\n\n"
            f"Получи шаблон для планирования + подарок (гайд по организации самообучения) навсегда за 30 ₽")

    keyboard = [
        [InlineKeyboardButton("Да", callback_data="advertisement_message_yes"),
         InlineKeyboardButton("Нет", callback_data="advertisement_message_no")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=reply_markup
    )

    return ADVERTISEMENT_MESSAGE


async def advertisement_message_back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    text = (f"Хочешь купить удобный шаблон, который поможет ещё более эффективно планировать задачи?\n\n"
            f"Получи шаблон для планирования + подарок (гайд по организации самообучения) навсегда за 30 ₽")

    keyboard = [
        [InlineKeyboardButton("Да", callback_data="advertisement_message_yes"),
         InlineKeyboardButton("Нет", callback_data="advertisement_message_no")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query

    await query.answer()
    await query.edit_message_text(
        text=text,
        reply_markup=reply_markup
    )

    return ADVERTISEMENT_MESSAGE
