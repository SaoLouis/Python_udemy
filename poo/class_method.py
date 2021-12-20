class Voiture:
	voiture_crees = 0
	def __init__(self, marque, vitesse, prix):
		Voiture.voiture_crees += 1
		self.marque = marque
		self.vitesse = vitesse
		self.prix = prix

#Méthodes de classe
	@classmethod
	def Lamborghini(cls):
		return cls(marque="Lamborghini",vitesse=200, prix=200000)

	@classmethod
	def Porsche(cls):
		return cls(marque="Lamborghini", vitesse=200, prix=180000)

#Méthode statique
	@staticmethod
	def afficher_nombre_voitures():
		print(f"Vous avez {Voiture.voiture_crees} voitures dans votres garages.")

lamborghini = Voiture.Lamborghini()
porsche = Voiture.Porsche()
Voiture.afficher_nombre_voitures()