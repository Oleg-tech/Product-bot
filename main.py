import db
from parse import schedule_parse
from administration import send_document, send_documents_for_admin
from config import bot, keyboard, keyboard_admin, keyboard_choose


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    db.insert_into_excel(msg.from_user.id, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.username)
    if msg.chat.id == -654118903:
        bot.reply_to(msg, "-_-", reply_markup=keyboard_admin)
        admin(msg)
    else:
        bot.reply_to(msg, "Привіт, " + msg.from_user.first_name, reply_markup=keyboard)


def admin(msg):
    if msg.text == 'Всі продукти':
        send_documents_for_admin()
    if msg.text == 'Користувачі':
        result = db.get_excel()
        bot.send_message(-654118903, result)
    if msg.text == 'Відправити повідомлення':
        bot.send_message(-654118903, "Виберіть умову", reply_markup=keyboard_choose)
    if msg.text == 'Вибрати користувача':
        result = db.get_excel()
        bot.send_message(-654118903, result)
        db.queu = True


@bot.message_handler(content_types=["text"])
def message(msg):
    db.insert_into_excel(msg.from_user.id, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.username)
    if msg.chat.id == -654118903:
        if db.queu is True:
            base = msg.text.split('\n')
            bot.send_message(db.find_user(base[0].strip()), base[1])
            db.queu = False
        admin(msg)
    else:
        if msg.text == 'Алкоголь':
            send_document(msg, msg.text)
        if msg.text == 'М`ясо':
            send_document(msg, msg.text)
        if msg.text == 'Соуси та консервація':
            send_document(msg, msg.text)


if __name__ == '__main__':
    bot.infinity_polling(
        schedule_parse()
    )
