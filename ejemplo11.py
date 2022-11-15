import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('insert into animal(name) values ("perro")')
cursor.execute('insert into animal(name) values ("gato")')
connection.commit()

connection.close()