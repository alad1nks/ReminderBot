from telegram import Update
from telegram.ext import Application, ConversationHandler, CommandHandler, filters, MessageHandler, \
    CallbackQueryHandler

from bot_token import TOKEN
from constants import COURSE_LINK, COURSE_NAME, COURSE_TIME, COURSE_DAYS, COURSE_RIGHT, CREATE_NEW_COURSE_OR_CHECK, \
    COURSE_LIST, EDIT_COURSE, DELETE_COURSE, COURSE_DELETED, REMIND_MESSAGE, COURSE_LINK_INVALID, COURSE_TIME_INVALID
from course_days import course_days, course_days_button
from course_deleted import course_deleted
from course_editing import course_editing
from course_link_invalid import course_link_invalid
from course_list import course_list
from course_name import course_name
from course_right import course_right
from course_time import course_time
from course_time_invalid import course_time_invalid
from create_new_course_or_check import create_new_course_or_check
from delete_course import delete_course
from edit_course import edit_course
from start import start, restart


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            COURSE_LINK: [
                MessageHandler(filters.TEXT & filters.Regex(r"https?://[^\s]+"), course_name),
                MessageHandler(filters.TEXT, course_link_invalid)
            ],
            COURSE_LINK_INVALID: [
                MessageHandler(filters.TEXT & filters.Regex(r"https?://[^\s]+"), course_name),
                MessageHandler(filters.TEXT, course_link_invalid)
            ],
            COURSE_NAME: [MessageHandler(filters.TEXT, course_time)],
            COURSE_TIME: [
                CallbackQueryHandler(restart),
                MessageHandler(filters.TEXT & filters.Regex(r"\b([01]?\d|2[0-3]):([0-5]?\d)\b"), course_days),
                MessageHandler(filters.TEXT, course_time_invalid)
            ],
            COURSE_TIME_INVALID: [
                MessageHandler(filters.TEXT & filters.Regex(r"\b([01]?\d|2[0-3]):([0-5]?\d)\b"), course_days),
                MessageHandler(filters.TEXT, course_time_invalid)
            ],
            COURSE_DAYS: [
                CallbackQueryHandler(course_right, pattern="next"),
                CallbackQueryHandler(course_time, pattern="back"),
                CallbackQueryHandler(course_days_button, pattern=r"\d+")
            ],
            COURSE_RIGHT: [
                CallbackQueryHandler(create_new_course_or_check, pattern="yes"),
                CallbackQueryHandler(course_days, pattern="back")
            ],
            CREATE_NEW_COURSE_OR_CHECK: [
                CallbackQueryHandler(restart, pattern="create"),
                CallbackQueryHandler(course_list, pattern="my_courses")
            ],
            COURSE_LIST: [
                CallbackQueryHandler(edit_course, pattern="edit"),
                CallbackQueryHandler(delete_course, pattern="delete"),
                CallbackQueryHandler(restart, pattern="create")
            ],
            EDIT_COURSE: [
                MessageHandler(filters.TEXT, course_editing),
                CallbackQueryHandler(course_list, pattern="back")
            ],
            DELETE_COURSE: [
                MessageHandler(filters.TEXT, course_deleted),
                CallbackQueryHandler(course_list, pattern="back")
            ],
            COURSE_DELETED: [
                CallbackQueryHandler(restart, pattern="create"),
                CallbackQueryHandler(course_list, pattern="my_courses")
            ],
            REMIND_MESSAGE: [
                CallbackQueryHandler(restart, pattern="create"),
                CallbackQueryHandler(course_list, pattern="my_courses")
            ]
        },
        fallbacks=[]
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


jobs_dict = {}

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text('Отправьте /schedule для планирования и /cancel для отмены задач.')
#
#
# async def schedule_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     try:
#         text = update.message.text.split()  # "HH:MM day1 day2 ..."
#         time_str = text[1]  # Время в формате "ЧЧ:ММ"
#         days = text[2:]  # Дни недели
#
#         hours, minutes = map(int, time_str.split(':'))
#         time = datetime.time(hour=hours, minute=minutes)
#
#         # Словарь для перевода дней недели
#         days_dict = {'пн': 1, 'вт': 2, 'ср': 3, 'чт': 4, 'пт': 5, 'сб': 6, 'вс': 0}
#
#         chat_id = update.effective_chat.id
#         jobs_dict[chat_id] = []
#
#         for day in days:
#             day_num = days_dict.get(day, None)
#             if day_num is not None:
#                 # Запланировать задачу и сохранить объект Job
#                 job = context.job_queue.run_daily(send_sas, time=time, days=(0, 1, 2, 3, 4, 5, 6), data=chat_id)
#                 jobs_dict[chat_id].append(job)
#
#         await update.message.reply_text('Сообщение будет отправляться каждую неделю в указанное время и дни.')
#     except Exception as e:
#         print(e)
#         await update.message.reply_text('Произошла ошибка при планировании сообщения. Проверьте формат данных.')
#
#
# async def send_sas(context: CallbackContext) -> None:
#     """Функция для отправки сообщения "САС"."""
#     chat_id = context.job.data
#     await context.bot.send_message(chat_id=chat_id, text="САС")
#
#
# async def cancel_jobs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     chat_id = update.effective_chat.id
#     if chat_id in jobs_dict and jobs_dict[chat_id]:
#         for job in jobs_dict[chat_id]:
#             job.schedule_removal()  # Отменяем задачу
#         jobs_dict[chat_id] = []  # Очищаем список задач для этого чата
#         await update.message.reply_text('Все запланированные сообщения были отменены.')
#     else:
#         await update.message.reply_text('Нет активных задач для отмены.')
#
#
# def main() -> None:
#     application = Application.builder().token(TOKEN).build()
#
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("schedule", schedule_message))
#     application.add_handler(CommandHandler("cancel", cancel_jobs))
#
#     application.run_polling()


if __name__ == "__main__":
    main()
