premier_nombre = input("Veuillez entrer un premier nombre: ")
deuxieme_nombre = input("Veuillez entrer un second nombre: ")
resultat = (int(premier_nombre) + int(deuxieme_nombre))
print(f"Le résutlat de l'adition de {premier_nombre} avec {deuxieme_nombre} est égal à {resultat}")

#Deuxieme version avec gestion d'erreur

premier_nombre = deuxieme_nombre = ""

while not (premier_nombre.isdigit() and deuxieme_nombre.isdigit()):

    premier_nombre = input("Veuillez entrer un premier nombre: ")
    deuxieme_nombre = input("Veuillez entrer un second nombre: ")
    resultat = ((premier_nombre) + (deuxieme_nombre))


    if not(premier_nombre.isdigit() and deuxieme_nombre.isdigit()):
        print("Veuillez entrer deux nombres valides")

print(f"Le résutlat de l'adition de {premier_nombre} avec {deuxieme_nombre} est égal à {int(premier_nombre) + int(deuxieme_nombre)}")

#Version allegé
while True:

    op_1 = input("Entrez un premier nombre : ")
    op_2 = input("Entrez un deuxième nombre : ")
    if not op_1.isdigit() or  not op_2.isdigit():
        print("Veuillez entrer deux nombres valides")
        continue
    break
print(f"Le résultat de l'addition de {op_1} avec {op_2} est égal à {int(op_1)+int(op_2)} ")