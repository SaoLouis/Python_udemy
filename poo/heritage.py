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

class Junior(Utilisateur):
	def __init__(self,nom,prenom):
		super().__init__(nom, prenom)

	def afficher_projet(self):
		for projet in projets:
			if not projet.startswith("pr_"):
				print(projet)

#Junior est l'héritage d'utilisateur
# class Junior(Utilisateur):
# 	def __init__(self,nom,prenom):
# 		Utilisateur.__init__(self, nom, prenom)

#Fonction super() récupère le nom de la classe parent
# class Vip(Utilisateur):
# 	def __init__(self, nom, prenom):
# 		super().__init__(nom, prenom)

paul = Junior("Paul","Durand")
pierre = Utilisateur("Pierre", "Dupond")
# jacque = Vip("Jacque", "Dutronc")
paul.afficher_projet()
