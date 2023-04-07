#Ordre de la matrice
ordre = int(input("Entrez l'odre de la matrice : "))

# Verifie si l'ordre est plus grand que  5
if ordre > 5:
  # choix de couleur
  choix_couleur = input("Entrez le choix de couleur(Bleu ou Rouge): ")
  # choix de position
  choix_position= input("Entrez le choix de position (Haut ou Bas): ")

  # Initialisation de la matrice par 0
  matrice = [[0 for x in range(ordre)] for y in range(ordre)]

  # boucle qui parcourt la matrice
  for i in range(ordre):
    for j in range(ordre):
      if choix_couleur == "Bleu" and choix_position == "Haut":
        if i < j:
          matrice[i][j] = "b"
      if choix_couleur== "Bleu" and choix_position == "Bas":
        if i > j:
          matrice[i][j] = "b"
      if choix_couleur== "Rouge" and choix_position == "Bas":
        if i>j:
          matrice[i][j] = "r"
      if choix_couleur== "Rouge" and choix_position == "Haut":
        if i<j:
          matrice[i][j]=='r'
         

  #Affiche la matrice
  print("Matrice obtenue :")
  for i in matrice:
    print(i)
else:
  # Le message d'erreur si l'ordre est moins grand que 5
  print("L'ordre doit etre supérieur à 5.")

