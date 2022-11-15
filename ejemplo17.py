import mysql.connector

#10.101.11.30
connection = mysql.connector.connect(host='10.101.11.30',port='3309',user='root',password='Ad1234' ,database='animal')

cursor = connection.cursor()

#cursor.execute('insert into animal(name) values ("gato")')
#connection.commit()
cursor.execute('select * from animal')
animals = cursor.fetchall()

for animal in animals:
    print(animal)

connection.close()