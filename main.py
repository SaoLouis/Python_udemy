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
commentaire= get_comment(20)
print(commentaire)