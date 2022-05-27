import xlsxwriter
import sqlite3
import json
# book = xlsxwriter.Workbook("Users.xlsx")
# users = book.add_worksheet("all_users")
# users.write("ID", "Name", "Surname", "Username")
# book.close()

queu = False
massage_for_user = ''


def get_excel():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    result = ''
    for i in sql.execute(f"SELECT id,username FROM Users"):
        result += str(i) + '\n'
    return result


def insert_into_excel(user_id, name, surname, username):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute('''CREATE TABLE IF NOT EXISTS Users(
        id INT,
        name VARCHAR(40),
        surname VARCHAR(40),
        username VARCHAR(40)
        )''')
    db.commit()
    sql.execute("SELECT id FROM Users WHERE id = ?", (user_id,))
    data = sql.fetchall()
    if len(data) == 0:
        sql.execute(f"INSERT INTO Users VALUES(?, ?, ?, ?)", (user_id, name, surname, username))
        db.commit()


def find_user(username):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute("SELECT id FROM Users WHERE username = ?", (username,))
    data = sql.fetchone()
    result = -654118903
    if data is not None:
        sql.execute("SELECT id FROM Users WHERE username = ?", (username,))
        result = (sql.fetchone())[0]
    print(result)
    return result


def db(names, old_prices, new_prices, category):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute('''DROP TABLE IF EXISTS products''')
    sql.execute('''CREATE TABLE IF NOT EXISTS products(
    name VARCHAR(40),
    old_price VARCHAR(10),
    new_price VARCHAR(10),
    category VARCHAR(15)
    )''')
    db.commit()

    for i in range(len(names)):
        sql.execute(f"INSERT INTO products VALUES(?, ?, ?, ?)", (names[i], old_prices[i], new_prices[i], category))
    db.commit()
