import telegram
from telegram import Update
from telegram.ext import ContextTypes

from constants import ADVERTISEMENT_THANKS


async def advertisement_thanks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    text = (f"Спасибо за покупку!\n\n<u>https://clck.ru/3B48aS</u> — шаблон для планирования\n\n"
            f"<u>https://clck.ru/3AzSSc</u> — гайд для самоорганизации обучения\n\nЖелаем тебе успехов 💖...")

    query = update.callback_query

    await query.answer()
    await query.edit_message_text(text=text, parse_mode=telegram.constants.ParseMode.HTML)

    return ADVERTISEMENT_THANKS
