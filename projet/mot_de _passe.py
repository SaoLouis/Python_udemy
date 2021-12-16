password = input("Entrez un mot de passe (min 8 caractères) : ")
password_trop_court = "votre mot de passe est trop court."

if len(password) == 0:
    print(password_trop_court.upper())
    exit()
elif len(password) < 8:
    print(password_trop_court.capitalize())
    exit()

if password.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
    exit()

print("Inscription terminée.")