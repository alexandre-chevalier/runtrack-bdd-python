import mysql.connector

myDb = mysql.connector.connect(
    user='root',
    password='root',
    database='laplateforme'
    )

mycursor = myDb.cursor()

mycursor.execute("select nom, capacite from salle")


for i in mycursor:
    print(i)