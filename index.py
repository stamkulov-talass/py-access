import pyodbc

try:
    driver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    path=r'DBQ=C:\Users\User\Desktop\db.accdb;'
    print(driver + path)
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' r'DBQ=C:\Users\User\projects\py-access\db.accdb;')
    cursor = conn.cursor()
    result = conn.execute('select * from студент')
    for row in result.fetchall():
        print(row)
    print("Connected To Database", result)


except pyodbc.Error as e:
    print("Error in Connection", e)