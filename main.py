class Voiture:
    def __init__(self):
        self.essence = 100

    def afficher_resevoir(self):
        print(f"La voiture contient x litres d’essence {self.essence}L d'essence")

    def roule(self, km):
        if self.essence <=0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return

        self.essence -= (km * 5) / 100
        if self.essence <10:
            print("Vous n'avez bientôt plus d'essence !")
        self.afficher_resevoir()
    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")