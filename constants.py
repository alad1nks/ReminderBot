import pytz

(COURSE_LINK, COURSE_LINK_INVALID, COURSE_NAME, COURSE_TIME, COURSE_TIME_INVALID, COURSE_DAYS, COURSE_RIGHT,
 CREATE_NEW_COURSE_OR_CHECK, COURSE_LIST, EDIT_COURSE, DELETE_COURSE, COURSE_DELETED, REMIND_MESSAGE) = range(13)

days = {
    '1': 'Понедельник',
    '2': 'Вторник',
    '3': 'Среда',
    '4': 'Четверг',
    '5': 'Пятница',
    '6': 'Суббота',
    '0': 'Воскресенье'
}

moscow_tz = pytz.timezone("Europe/Moscow")
