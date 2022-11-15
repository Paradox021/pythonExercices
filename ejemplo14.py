import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

animal = cursor.execute('select * from animal where id=2').fetchone()
print(animal)

connection.close()