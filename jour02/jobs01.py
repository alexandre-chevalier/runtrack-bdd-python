import mysql.connector

myDb = mysql.connector.connect(
    user='root',
    password='root',
    database='laplateforme'
    )

mycursor = myDb.cursor()

mycursor.execute("select * from etudiant")


for i in mycursor:
    print(i)