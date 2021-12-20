# class Voiture:
#     marque = "Lamborghini"
#
# voiture_01 = Voiture()
#

# class Employee:
#     first_name = "John"
#     last_name = "Smith"
#
# employee_01 = Employee()
# employee_02 = Employee()
# print(employee_01.first_name,employee_01.last_name + " " + employee_02.first_name + " " + employee_02.last_name)

# class Voiture:
#     marque = ""
#
# voiture_01 = Voiture()
# voiture_02 = Voiture()
#
# voiture_01.marque = "Peugeol"
# voiture_02.marque = "Volkswagen"
#
# print(voiture_01.marque)
# print(voiture_02.marque)


#Une voiture avec marque, couleur et modele
class Voiture:
    def __init__(self, marque, couleur, modele):
        self.marque = marque
        self.couleur = couleur
        self.modele = modele

voiture_01 = Voiture("Lamborghini", "rouge", "Avantador" )
# voiture_02 = Voiture("Porsche")

print(voiture_01.marque+", "+ voiture_01.couleur+", "+ voiture_01.modele)
# print(voiture_02.marque)

#Exercice livre
class Livre:
    def __init__(self, nom, nombre_de_pages, prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix

livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LOTR = Livre("Le Seigneur des Anneaux", 400, 13.99)

#self
class Voiture :
    def __init__(self, marque):
        self.marque = marque
    def afficher_marque(self):
        print(f"La voiture est une {self.marque}")

voiture_01 = Voiture("Lamborghini")
voiture_01.afficher_marque()
Voiture.afficher_marque(voiture_01)



