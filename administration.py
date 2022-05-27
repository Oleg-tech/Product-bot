from config import files, ADMIN_CHAT, bot, keyboard, keyboard_admin


def send_document(message, key):
    file = open(files[key], 'rb')
    bot.send_document(message.chat.id, file, reply_markup=keyboard)
    file.close()


def send_documents_for_admin():
    for link in files:
        file = open(files[link], 'rb')
        bot.send_document(ADMIN_CHAT, file, reply_markup=keyboard_admin)
        file.close()