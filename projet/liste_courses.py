# import sys
#
# LISTE = []
#
# MENU = """Choisissez parmi les 5 options suivantes :
# 1: Ajouter un élément à la liste
# 2: Retirer un élément de la liste
# 3: Afficher la liste
# 4: Vider la liste
# 5: Quitter
# ? Votre choix : """
#
# MENU_CHOICES = ["1", "2", "3", "4", "5"]
#
#
#
# while True:
#     user_choice = input(MENU)
#     if user_choice not in MENU_CHOICES:
#         print("Veuillez choisir une option valide...")
#         continue
#
#     if user_choice == "1":  # Ajouter un élément
#         item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
#         LISTE.append(item)
#         print(f"L'élément {item} a bien été ajouté à la liste.")
#     elif user_choice == "2":  # Retirer un élément
#         item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
#         if item in LISTE:
#             LISTE.remove(item)
#             print(f"L'élément {item} a bien été supprimé de la liste.")
#         else:
#             print(f"L'élément {item} n'est pas dans la liste.")
#     elif user_choice == "3":  # Afficher la liste
#         if LISTE:
#             print("Voici le contenu de votre liste :")
#             for i, item in enumerate(LISTE, 1):
#                 print(f"{i}. {item}")
#         else:
#             print("Votre liste ne contient aucun élément.")
#     elif user_choice == "4":  # Vider la liste
#         LISTE.clear()
#         print("La liste a été vidée de son contenu.")
#     elif user_choice == "5":  # Quitter
#         print("À bientôt !")
#         sys.exit()
#
#     print("-" * 50)


# Liste de course deuxieme version

import logging

LOGGER = logging.getLogger()


class Liste(list):
	def __init__(self, nom):
		self.nom = nom

	def ajouter(self, element):
		if not isinstance(element, str):
			raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères!")

		if element in self:
			LOGGER.error(f"{element} est déjà dans la liste.")
			return False

		self.append(element)
		return True

	def enlever(self, element):
		if element in self:
			self.remove(element)
			return True
		return False

	def afficher(self):
		print(f"Ma liste de {self.nom} :")
		for element in self:
			print(f" - {element}")


if __name__ == "__main__":
	liste = Liste("taches")
	liste.ajouter("Pommes")
	liste.ajouter("Poires")
	liste.afficher()