from telegram import Update
from telegram.ext import ContextTypes

from constants import ADVERTISEMENT_THANKS


async def advertisement_thanks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    text = (f"Спасибо за покупку!\n\nhttps://clck.ru/3B48aS— шаблон для планирования https://clck.ru/3AzSSc — гайд для "
            f"самоорганизации обучения Желаем тебе успехов 💖")

    query = update.callback_query

    await query.answer()
    await query.edit_message_text(text=text)

    return ADVERTISEMENT_THANKS
