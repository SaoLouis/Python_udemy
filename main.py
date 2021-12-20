class Client:
	def __init__(self, nom, prenom, age, ville):
		self.nom = nom
		self.prenom = prenom
		self.age = age
		self.ville = ville

	def __str__(self):
		return f"Le client {self.nom} {self.prenom} agé de {self.age} habite à {self.ville}."

client_01 = Client("Doe", "John", 27, "Bordeaux")

affichage = str(client_01)

print(affichage)