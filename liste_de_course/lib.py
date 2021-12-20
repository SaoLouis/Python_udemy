import json
import logging
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()


class Liste(list):
	def __init__(self, nom):
		super().__init__()
		self.nom = nom
#Ajoute un élément dans la liste
	def ajouter(self, element):
		if not isinstance(element, str):
			raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères!")

		if element in self:
			LOGGER.error(f"{element} est déjà dans la liste.")
			return False

		self.append(element)
		return True
#Enlève un élement de la liste
	def enlever(self, element):
		if element in self:
			self.remove(element)
			return True
		return False
#Afficher le contenu de la liste
	def afficher(self):
		print(f"Ma liste de {self.nom} :")
		for element in self:
			print(f" - {element}")

#Sauvegarde des élément ajouter dans la liste
	def sauvegarder(self):
			chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
			if not os.path.exists(DATA_DIR):
				os.makedirs(DATA_DIR)

			with open(chemin, "w") as f:
				json.dump(self, f, indent=4)

			return True


if __name__ == "__main__":
	liste = Liste("courses")
	liste.ajouter("Pommes")
	liste.ajouter("Poires")
	liste.sauvegarder()