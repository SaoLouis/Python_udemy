#Afficher la table de multiplication
nombre = 7

for i in range(11):
    print(f"{i} x {nombre} = {i * nombre}")

#Remplacement d'une boucle par une compréhensions de liste
liste = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nombres_pairs = [i for i in liste if i % 2 == 0]
print(nombres_pairs)

nombres = range(-10, 10)
nombres_positifs = []
nombres_positifs = [i for i in nombres if i >= 0]
print(nombres_positifs)

nombre = range(5)
nombres_doubles = []
nombres_doubles = [i * 2 for i in nombre]
print(nombres_doubles)

number = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in number]
print(nombres_inverses)

#Nombres pair
nombres = range(51)
nombres_pairs = []

for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)
    print(nombres_pairs)


# Récuperation d'info dans un dictionnaire
employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
del employes["id03"]
employes["id02"]["age"] = 26
age_paul = employes["id01"]["age"]
print(employes)
print(age_paul)



#Voiture
class Voiture:
    def __init__(self):
        self.essence = 100

    def afficher_resevoir(self):
        print(f"La voiture contient x litres d’essence {self.essence}L d'essence")

    def roule(self, km):
        if self.essence <=0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return

        self.essence -= (km * 5) / 100
        if self.essence <10:
            print("Vous n'avez bientôt plus d'essence !")
        self.afficher_resevoir()
    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")