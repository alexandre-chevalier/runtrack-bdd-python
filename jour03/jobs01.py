import tkinter as  tk 
from tkinter import ttk
import mysql.connector

# select * from employe where salaire > 3000;
class Product:
    def __init__(self):
        self.myDb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="store"
        )
        self.cursor = self.myDb.cursor()
        self.listeProduit = []


    def create(self, nom, description, price,quantity, id_category):

        query = 'insert into product (name,description,price, quantity,  id_category) values (%s,%s,%s,%s,%s)'
        self.cursor.execute(query, (nom,description,price,quantity, id_category))
        self.myDb.commit()

    
    def read(self):
        self.cursor.execute( 'select product.id, product.name, description, price, quantity,category.id, category.name from product inner join category on product.id_category = category.id;')
        for i in self.cursor:
            product = {
                'id':i[0],
                'nom':i[1],
                'description':i[2],
                'price':i[3],
                'quantity':i[4],
                'id_category':i[5],
                'category_name':i[6]
            }
            self.listeProduit.append(product)
        


    def update(self, nom,description,price,quantity, id):
        query = 'update product set name = %s , desciption = %s , price = %s , quantity = %s where id = %s'
        self.cursor.execute(query, (nom,description,price,quantity, id))
        self.myDb.commit()

    def delete(self,id):
        query = 'delete from product where id = %s'
        self.cursor.execute(query, (id,))
        self.myDb.commit()

    def close_connection(self):
        self.cursor.close()
        self.myDb.close()

def clavier(event):
    souris = event.keysym
    print(souris)






WIDTH = 600
HEIGHT = 400
produit = Product()
produit.read()

fenetre = tk.Tk()
fenetre.geometry(f"{WIDTH}x{HEIGHT}")
fenetre.title("Gestion de Stock")

menu_bar = tk.Menu(fenetre)

menu = tk.Menu(menu_bar, tearoff=0)
menu.add_command(label="Liste de produit")
menu.add_command(label="Creer un produit")
menu.add_command(label="Supprimer un produit")
menu.add_command(label="Maj Produit")
menu.add_separator()
menu.add_command(label="Quitter", command=fenetre.quit)
menu_bar.add_cascade(label="Menu", menu=menu)

fenetre.config(menu=menu_bar)

tableau = ttk.Treeview(fenetre, columns=("id_produit","nom","description","price","quantite","id_category","nom_categorie"))
tableau.heading("id_produit", text="id_produit")
tableau.heading("nom", text="nom")
tableau.heading("description", text="description")
tableau.heading("price", text="price")
tableau.heading("quantite", text="quantite")
tableau.heading("id_category", text="id_category")
tableau.heading("nom_categorie", text="nom_categorie")
tableau.pack(fill=tk.BOTH, expand=True)


for product in produit.listeProduit:
    tableau.insert(
        "",
        "end",
        values=(
            product["id"],
            product["nom"],
            product["description"],
            product["price"],
            product["quantity"],
            product["id_category"],
            product["category_name"],
        ),
    )
        
btn = tk.Button(fenetre, text="Liste de produits")
btn.pack(side='bottom', anchor='w', padx=10, pady=10)


fenetre.mainloop()