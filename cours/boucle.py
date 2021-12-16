#For
races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

#Parcours un char
for lettres in "Python":
    print(lettres)
#Range (créer 10 fois bonjour)
for i in range(10):
    print("Bonjour")

#While 
capacite_maximal = 10
capacite_actuel = 3
while capacite_actuel < capacite_maximal:
    capacite_actuel += 1
    print (capacite_actuel)
#-----------------------------------"
i = 0
while i < 10:
    print("Bonjour")
    i += 1

#Bouton continuer
continuer = "o"
while continuer == "o":
    print("On continue...")
    continuer = input("Voules vous continuer ? o/n ")


#For/else
prenoms = ["Pierre", "Patrick", "Jean", "Marc"]

for prenom in prenoms:
    if prenom == "Patrick":
        print("Patrick a été trouvé !")
        break
else:
        print("Patrick est introuvable...")

#Compréhension de liste
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombre_positifs = [i for i in liste if i > 0]

#Any (check si une valeurs est vrais)
notes = [12,14,20,10,8]
any([x > 18 for x in notes])