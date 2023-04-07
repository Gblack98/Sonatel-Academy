# Définir une liste pour stocker les numéros valides
numeros_valides = []
numeros_invalides=[]

# Définir un dictionnaire pour compter le nombre de numéros pour chaque opérateur
operateurs = {}

# Demander à l'utilisateur de saisir une chaîne contenant les numéros
chaine = input("Saisissez une chaîne contenant des numéros : ")

# Séparer les numéros dans la chaîne
numeros = chaine.split('#')


# Pour chaque numéro dans la liste
for numero in numeros:
    # Vérifier si le numéro est valide (10 chiffres)
    if len(numero) == 9 and (numero[:2]=="70" or numero[:2]=="75" or numero[:2]=="76" or numero[:2]=="77" or numero[:2]=="78"):
        # Ajouter le numéro à la liste des numéros valides
        numeros_valides.append(numero)
        # Déterminer l'opérateur à partir des 3 premiers chiffres du numéro
        operateur = numero[:2]
        # Mettre à jour le dictionnaire pour compter le nombre de numéros pour chaque opérateur
        if operateur in operateurs:
            operateurs[operateur] += 1
        else:
            operateurs[operateur] = 1
    else:
        # Sinon, le numéro est invalide
        # Ajouter le numéro à la liste des numéros invalides
        numeros_invalides.append(numero)

# Afficher les numéros valides à gauche de l'écran
print("Numéro(s) valide(s) : ", numeros_valides)
# Afficher les numéros invalides à droite de l'écran
print("Numéro(s) invalide(s) : ", numeros_invalides)
# Afficher le nombre de numéros de chaque opérateur
for operateur, nombre in operateurs.items():
    print("Opérateur",operateur,":", nombre,"numéro(s)")
