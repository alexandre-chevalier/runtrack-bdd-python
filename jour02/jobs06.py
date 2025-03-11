import mysql.connector

myDb = mysql.connector.connect(
    user='root',
    password='root',
    database='laplateforme'
    )

mycursor = myDb.cursor()

mycursor.execute("select sum(capacite) from salle")

for i in mycursor:
    print(f'la capacite de toutes les salles est de :  {i[0]}')