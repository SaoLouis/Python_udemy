class Vehicule:
	def avance(self):
		print("Le vehicule démarre")

#super().avance() = Polymorphisme | appel la methode parent et l'augmente dans la methode enfant
class Voiture(Vehicule):
	def avance(self):
		super().avance()
		print("La voiture roule")

class Avion(Vehicule):
	def avance(self):
		super().avance()
		print("L'avion vol")

v = Voiture()
a = Avion()
a.avance()