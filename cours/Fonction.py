# Retourner une valeur
def element():
	return 5


a = element()

print(a)


# Paramètres et arguments
def affiche(message):
	print(message)


affiche("Bonjour")


# --------------------------------------------
def affiche(message="Message par défaut"):
	print(message)


affiche()


# --------------------------------------------
def addition(a, b):
	return a + b


addition(b=10, a=5)

# Afficher une variable
ma_variable = 10


def afficher_variable():
	print(ma_variable)


afficher_variable()


# Globals
def foo():
	b = 5


a = 10
foo()
print(globals())


# instruction global (a ne pas utiliser)
def get_comment(note):
	global avis
	if note > 15:
		avis = "Bravo"
	elif note > 10:
		avis = "Peut mieux faire..."
	elif note > 5:
		avis = "Attention !"
	else:
		avis = "Tu as tout faux"
	return avis


commentaire = get_comment(20)
print(commentaire)


# instructions à utilisers
def get_comment(note):
	if note > 15:
		avis = "Bravo"
	elif note > 10:
		avis = "Peut mieux faire..."
	elif note > 5:
		avis = "Attention !"
	else:
		avis = "Tu as tout faux"
	return avis


commentaire = get_comment(10)
print(commentaire)


# Exercice sur les fonctions
def saluer(message):
	print("Bonjour", message)


saluer("Patrick")


# -------------------------
def addition(a, b):
	c = a + b
	return c


resultat = addition(5, 10)
print(resultat)
