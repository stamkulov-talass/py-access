import db_connection
class Student: 
    def insert(id, name, group, phone_number, birth_date, adress, date_of_receipt):
        result = db_connection.execute('insert into студент("код студент", "код группы", "ФИО", "День рождения", "Адрес", "Номер", "год поступления") values (?, ?, ?, ?, ?, ?, ?)', (id, group, name, birth_date, adress, phone_number, date_of_receipt))
        db_connection.commit()
        return result
    
    def update(id, name, group, phone_number, birth_date, adress, date_of_receipt):
        result = db_connection.execute('update студент set "код группы" = ?, "ФИО" = ?, "День рождения" = ?, "Адрес" = ?, "Номер"  = ?, "год поступления" = ? where "код студент" = ?', group, name, birth_date, adress, phone_number, date_of_receipt, id)
        db_connection.commit()
        return result
    
    def delete(id):
        result = db_connection.execute('delete from студент where "код студент" = ?', id)
        db_connection.commit()
        return result
    
    def select():
        return db_connection.execute('select * from студент')
    
    def selectOne(id):
        return db_connection.execute('select * from студент where "код студент" = ?', id)