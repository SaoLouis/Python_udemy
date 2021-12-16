nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne",
    "nom_de_campagne": "Campagne nous aimons les animaux",
    "date_de_debut": "01/01/2020",
    "influenceurs_importants":["@MonAmourDeChien", "@MeilleurFriandise"]
}
#-------------------------------------------------------
taux_de_conversations= {}
taux_de_conversations['facebook'] = 3.4

print(nouvelle_campagne["responsable_de_campagne"])
print(taux_de_conversations["facebook"])
#--------------------------------------------------------------
chaussure = {}
chaussure['taille'] = 42

taille = chaussure['taille']

print(taille)
#--------------------------------------------------------------
#Dictionnaire contenant plusieur clé/valeur
employer = {
    0:  {"prenom": "Louis",
         "proffession": "Ingénieur recette",
         "ville": "Bordeaux"},
    1:  {"prenom": "Camille",
         "Proffession": "null",
         "ville": "la Rochelle"},
    2:  {"prenom": "Pierre",
         "proffession": "Plombier",
         "ville": "Nantes"}
}
print(employer[2])

#Modification d'une valeur d'un dictionnaire
employer = {"prenom": "Louis",
            "proffession": "Ingénieur recette",
         "ville": "Bordeaux",

}
employer["prenom"] = "Julie"
print(employer)

# Prix de l'enssemble de film
films = {"Le Seigneur des Anneaux": 12,
         "Harry Potter": 9,
         "Blade Runner": 7.5}
prix = 0

for key in films:
    prix += films[key]
    print(prix)

#Supprimer une clé dans un dictionnaire
employer = {"prenom": "Louis",
         "proffession": "Ingénieur recette",
         "ville": "Bordeaux",

}
del employer["ville"]
print(employer)
# Si la clé age est présente
employer = {"prenom": "Louis",
         "proffession": "Ingénieur recette",
         "ville": "Bordeaux",
            "age": 30

}
if "age" in employer:
    del employer["age"]
print(employer)

# Ajoute une clé si elle n'est pas présente dans un dictionnaire
employer = {"prenom": "Louis",
         "proffession": "Ingénieur recette",
         "ville": "Bordeaux"

}
if "age" not in employer:
    employer["age"] = 30
print(employer)


