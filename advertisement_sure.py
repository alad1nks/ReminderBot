import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from constants import ADVERTISEMENT_SURE


async def advertisement_sure(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = ("Ты покупаешь <b>шаблон для планирования за 30 ₽</b>.  В покупку входит шаблон на платформе Notion и гайд "
            "для самоорганизации обучения в подарок.\n\nСсылка на оплату "
            "<u>https://yoomoney.ru/fundraise/132SFMFDFEI.240531</u>\n\n❗️После оплаты пришли скриншот платежа (чек) и "
            "нажми кнопку «Проверить»")

    keyboard = [
        [InlineKeyboardButton("Проверить", callback_data="advertisement_sure_next"),
         InlineKeyboardButton("Назад", callback_data="advertisement_sure_back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query

    await query.answer()
    await query.edit_message_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode=telegram.constants.ParseMode.HTML
    )

    return ADVERTISEMENT_SURE
