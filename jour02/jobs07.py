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
        cursor, _ = connex
        id =int(input('veuillez entrez un id : '))
        nom = input('veuillez entrez le nom de votre employe : ')
        prenom = input('veuillez entrez le prenom de votre employe : ')
        salaire = int(input('veuillez entrez votre salaire'))
        id_service = int(input("veuillez entrez le numero de service : "))

        query = 'insert into employe values (%s,%s,%s,%s,%s)'
        cursor.execute(query, (id,nom,prenom,salaire, id_service))

    
    def read(self, connex):
        cursor, _ = connex
        cursor.execute('select * from employe')

        for i in cursor:
            print(i)


    def update(self, connex):
        cursor, _ = connex
        salaire = int(input('veuillez entrez le nouveau prenom : '))
        id = int(input('veuillez entrez lid que vous voulez modifier : '))
        cursor.execute(f'update employe set salaire = {salaire} where id = {id}')

    def delete(self, connex):
        cursor, _ = connex
        id = int(input('veuillez entrez l id que vous voulez modifier : '))
        cursor.execute(f'delete from employe where id = {id}')



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