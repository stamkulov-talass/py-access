import pyodbc #модуль подключения к бд
import sys #модуль системы
conn = {} #создаём пустую переменну
try:
    # если подключение прошло успешно переменная conn будет равна подключению
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' r'DBQ=C:\Users\User\projects\py-access\db.accdb;')

except pyodbc.Error as e:
    # если во время подключения будут ошибки то код остановится
    print("Error in Connection", e)

# экспоритрование переменной conn
sys.modules[__name__] = conn