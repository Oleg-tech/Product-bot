import telebot
from telebot import types


bot = telebot.TeleBot('1842681158:AAHQSl6sn47NdaNk3Gf29nHIf8nL3X9DDeA')

SILPO = {
    'https://shop.silpo.ua/all-offers?filter_CATEGORY=(22)': 'alcohol',
    'https://shop.silpo.ua/all-offers?filter_CATEGORY=(316__277)': 'meat',
    'https://shop.silpo.ua/all-offers?filter_CATEGORY=(130)': 'sauce'
}

ADMIN_CHAT = '-654118903'
ADMIN_ID = '443648217'

files = {
    'Алкоголь': 'files/Silpo_alcohol.txt',
    'М`ясо': 'files/Silpo_meat.txt',
    'Соуси та консервація': 'files/Silpo_sauce.txt'
}

keyboard_admin = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
keyboard_admin.row('Всі продукти').row('Користувачі').row('Відправити повідомлення')

keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard.row('Алкоголь').row('М`ясо').row('Соуси та консервація')

keyboard_choose = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_choose.row('Вибрати користувача').row('Всім')
