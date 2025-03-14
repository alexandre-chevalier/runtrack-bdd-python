import mysql.connector

myDb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='root',
    database='laplateforme'
    )

mycursor = myDb.cursor()

mycursor.execute("select sum(superficie) from etage")

for i in mycursor:
    print(f'la superficie de la plateforme est de {i[0]}')