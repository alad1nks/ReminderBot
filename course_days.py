from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from constants import COURSE_DAYS


async def course_days(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    user_data['selected_options'] = set()
    user_data['course_days'] = []
    text = 'В какие дни хочешь заниматься по такому расписанию?'
    keyboard = [
        [InlineKeyboardButton('❌ Понедельник', callback_data='1'),
         InlineKeyboardButton('❌ Вторник', callback_data='2'),
         InlineKeyboardButton('❌ Среда', callback_data='3')],
        [InlineKeyboardButton('❌ Четверг', callback_data='4'),
         InlineKeyboardButton('❌ Пятница', callback_data='5'),
         InlineKeyboardButton('❌ Суббота', callback_data='6')],
        [InlineKeyboardButton('❌ Воскресенье', callback_data='0'),
         InlineKeyboardButton('Назад', callback_data='back'),
         InlineKeyboardButton('Далее', callback_data='next')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = update.message
    if message is None:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text=text,
            reply_markup=reply_markup
        )
    else:
        course_time = message.text
        user_data['course_time'] = course_time
        await update.message.reply_text(
            text=text,
            reply_markup=reply_markup
        )
    return COURSE_DAYS


async def course_days_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    query = update.callback_query
    selected_options = user_data['selected_options']
    await query.answer()
    if query.data in selected_options:
        selected_options.remove(query.data)
    else:
        selected_options.add(query.data)

    keyboard = []
    for row in query.message.reply_markup.inline_keyboard:
        new_row = []
        for button in row:
            if button.callback_data == query.data:
                day_text = button.text[1:]
                new_button = InlineKeyboardButton(
                    text=f"✅{day_text}" if query.data in selected_options else f"❌{day_text}",
                    callback_data=button.callback_data
                )
            else:
                new_button = InlineKeyboardButton(
                    text=button.text,
                    callback_data=button.callback_data
                )
            new_row.append(new_button)
        keyboard.append(new_row)

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_reply_markup(reply_markup=reply_markup)

    return COURSE_DAYS
