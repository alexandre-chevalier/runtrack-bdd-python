import mysql.connector

# select * from employe where salaire > 3000;
class Employe:
    def connexion(self):
        myDb = mysql.connector.connect(
            user='root',
            password='root',
            database='entreprise'
            )
        cursor = myDb.cursor()
        return cursor, myDb

    def create(self,connex):
        cursor, myDb  = connex
        nom = input('veuillez entrez le nom de votre employe : ')
        prenom = input('veuillez entrez le prenom de votre employe : ')
        salaire = int(input('veuillez entrez votre salaire'))
        id_service = int(input("veuillez entrez le numero de service : "))

        query = 'insert into employe (nom,prenom,salaire, id_service) values (%s,%s,%s,%s)'
        cursor.execute(query, (nom,prenom,salaire, id_service))
        myDb.commit()

    
    def read(self, connex):
        cursor, myDb  = connex
        cursor.execute('select * from employe')
        for i in cursor:
            print(i)
        myDb.commit()


    def update(self, connex):
        cursor, myDb  = connex
        salaire = int(input('veuillez entrez le nouveau salaire : '))
        id = int(input('veuillez entrez lid que vous voulez modifier : '))
        query = 'update employe set salaire = %s where id = %s'
        cursor.execute(query, (salaire, id))
        myDb.commit()

    def delete(self, connex):
        cursor, myDb = connex
        id = int(input('veuillez entrez l id que vous voulez supprimer : '))
        query = 'delete from employe where id = %s'
        cursor.execute(query, (id,))
        myDb.commit()



employe = Employe()
connexion = employe.connexion()

employe.read(connexion)
employe.create(connexion)
employe.read(connexion)
employe.update(connexion)
employe.read(connexion)
employe.delete(connexion)
employe.read(connexion)








## mycursor.execute("select * from employe where salaire > 3000;")

## mycursor.execute(' select employe.nom as nom_employe, prenom, service.nom from employe inner join service on employe.id_service = service.id;')