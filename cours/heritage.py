projets = ["pr_GameOfThrones", "Harry Potter", "pr_Avengers"]

class Utilisateur:
	def __init__(self, nom, prenom):
		self.nom = nom
		self.prenom = prenom

	def __str__(self):
		return f"Utilisateur {self.nom} ({self.prenom})"

	def afficher_projet(self):
		for projet in projets:
			print(projet)

#Junior est l'héritage d'utilisateur
class Junior(Utilisateur):
	pass


paul=Junior("Paul", "Durand")
paul.afficher_projet()