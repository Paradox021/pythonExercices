import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

animals = cursor.execute('select * from animal')
for animal in animals:
    print(animal)

connection.close()