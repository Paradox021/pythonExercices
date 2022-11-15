import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('update animal set name="cat" where id = 2' )
connection.commit()

connection.close()