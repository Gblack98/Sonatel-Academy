#Initialisation des couleurs dans la liste
couleurs = ["rouge", "bleue", "jaune", "verte", "mauve", "noire"]

#Initialisation de la position des elements
positions = ["ADDP", "EDDP", "SDP", "ADDS", "EDDS", "SDS"]

#Ordre dela matrice
ordre = int(input("Entrez l'ordre de la matrice : "))

#Vérification de l'ordre qui doit etre sup&rieur à 4
if ordre <= 4:
  print("L'ordre de la matrice doit etre superieur à 4")
else:
  #On demande à l'utilisateur de choisir une position
  print("Choisir une position :")
  for i in range(len(positions)):
    print(f"{i + 1}. {positions[i]}")
  choix_position = int(input("Entrez votre choix de position : ")) - 1
  #On demande à l'utilisateur de choisir une couleur
  print("Choisis une couleur :")
  for i in range(len(couleurs)):
    print(f"{i + 1}. {couleurs[i]}")
  choix_couleur = int(input("Entrez votre choix de couleur : ")) - 1
  #On dessine la matrice
  for i in range(ordre):
    for j in range(ordre):
      if positions[choix_position] == "ADDP" and i < j:
        print(couleurs[choix_couleur], end=" ")
      elif positions[choix_position] == "EDDP" and i > j:
        print(couleurs[choix_couleur], end=" ")
      elif positions[choix_position] == "SDP" and i == j:
        print(couleurs[choix_couleur], end=" ")
      elif positions[choix_position] == "ADDS" and i + j == ordre - 1:
        print(couleurs[choix_couleur], end=" ")
      elif positions[choix_position] == "EDDS" and i + j != ordre - 1:
        print(couleurs[choix_couleur], end=" ")
      elif positions[choix_position] == "SDS" and i + j == ordre - 1:
        print(couleurs[choix_couleur], end=" ")
      else:
        print("0"+" "*(len(couleurs[choix_couleur])-1), end=" ")
    print()
