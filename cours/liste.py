#Liste
liste = [1 , 2 , 3 , 4 , 5]
liste_2=[250, "Pyhton", True]
print(liste_2)
print(liste)

#Tuple 
mon_tuple = (1, 2, 3, 4, 5)
mon_tuple_2 =(250, "Pyhton", True)

#Convertion tuple vers liste
mon_tuple =(1 , 2 , 3 , 4 , 5)
liste = list(mon_tuple)
print(liste)

#Convertion liste vers tuple
mon_tuple = tuple(liste)
print(mon_tuple)

#ajouter un seul élément à une liste
liste = [1 , 2 , 3 , 4 , 5]
liste.append(6)
print(liste)

#Ajouter plusieueurs élément à une liste
liste = [1 , 2 , 3 , 4 , 5]
liste.extend([6, 7, 8])
print(liste)

#Enlever un élément de la liste
liste = [1, 2, 3, 4, 5]
liste.remove(5)
print(liste)

#Recuperer élément de la liste
liste = ["Python",["C#"],"Java", "JavaScript"]
print(liste[1][0])

#Slice
liste = ["Utilisateur_01",
         "Utilisateur_02",
         "Utilisateur_03",
         "Utilisateur_04",
         "Utilisateur_05",
         "Utilisateur_06"]
print(liste[0:3])

#exercice
"""liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[:3]
trois_derniers = liste[3:]
milieu = liste[1:-1]
premier_dernier = liste[::5] """

#indexes
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
resultat = employes.index("Alex")
print(resultat)

#occurence
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
resultat = employes.count("Alex")
print(resultat)

#Trie alphabetique
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.sort()
print(employes)

#Pop (index)
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.pop(-1)
print(employes)

#Pop (élement)
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
element = employes.pop(-1)
print(element)

#Clear (supprimer la liste)
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.clear()
print(employes)

#Join
liste = ["Python", "est", "un", "langage", "incroyable"]
resultat =  "\n".join(liste)

print(resultat)

#Split
courses = "Riz, Pomme, Lait, Salade, Saumon, Beurre"
courses = courses.split(", ")
print(courses)

#Liste imbriquées
liste = ["Python",["Java", "C++", ["C"]], ["Ruby"]]
print(liste[2][0])
