# Импорт библиотеки
import sqlite3
# Подключение к БД
con = sqlite3.connect("userSpecifications.db")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
lastName = cur.execute("""SELECT name FROM user
            WHERE id = 1""").fetchall()[0][0]
lastAge = cur.execute("""SELECT age FROM user
            WHERE id = 1""").fetchall()[0][0]
lastMoney = cur.execute("""SELECT money FROM user
            WHERE id = 1""").fetchall()[0][0]

con.close()
