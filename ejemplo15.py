import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('delete from animal where id=1')
connection.commit()
print("animal con id 1 borrado")

animals = cursor.execute('select * from animal')
for animal in animals:
    print(animal)


connection.close()