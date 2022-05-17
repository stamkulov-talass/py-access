import numbers
import string
import db_connection
# result это переменна
# exexute это метод для запуска запросовиз 
# result = db_connection.execute('select * from студент')

# #цикл который пробегается по массиву данных result 
# for row in result.fetchall():
#     print(row)

def insert(name):
    return db_connection.execute("insert into студент(ФИО) values (?)", (name))


def update(id: numbers, name: string):
    result = db_connection.execute('update студент set ФИО=? where "код студент"=?', name, id)
    db_connection.commit()
    return result


def select():
    return db_connection.execute('select ФИО from студент where "код студент"=65')

# for row in select().fetchall():
#     print(row)
update(12, 'Beka')