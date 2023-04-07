#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tabulate import tabulate
def Correction_Num (num):
  correction=""
  for i in num:
    if i==" ":
      continue
    else:
      correction+=i
  return correction 

def taille(num):
  if len(num)==7:
    return True
  else:
    return False  

def valide_num(num):
    for i in num:
        if (('i'>='A' and 'i'<='Z') or ('i'>='a' and 'i'<='z') or ('i'>='0' and 'i'<='9')):
            if taille(num)==True:
                return True
           
        return False

def Prenom(prenom):
    #initialisation
    cpt=0
    #on compte le nombre de lettre dans le prenom
    if prenom[0]>='A' and prenom[0]<='Z' or (prenom[0]>='a'and prenom[0]<='z'):
        for i in prenom:
            if ('i'>='A'and 'i'<='Z')or ('i'>='a'and 'i'<='z'):
                cpt+=1
    if cpt>=3:
        return True
    return False

def Nom(nom):
    #initialisation
    cpt=0
    #on compte le nombre de lettre dans le nom
    if nom[0]>='A' and nom[0]<='Z' or (nom[0]>='a'and nom[0]<='z'):
        for i in nom:
            if (i>='A'and i<='Z') or (i>='a'and i<='z'):
                cpt+=1
    #si on trouve plus de deux, alors le nom est valide 
    if cpt>=2:
        return True
    return False

def Valide_date(jour,mois,annee):
    # Vérification des limites de la date
    if annee < 1 or mois < 1 or mois > 12 or jour < 1 or jour > 31:
        return False
    
    # Vérification de février en fonction des années bissextiles
    if mois == 2:
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            if jour > 29:
                return False
        elif jour > 28:
            return False
    
    # Vérification des mois avec 30 jours
    if mois in [4, 6, 9, 11]:
        if jour > 30:
            return False
    
    return True

def Valide_Classe(classe):
    classe=classe.strip(" ")
    if (classe[0]>='1' and classe[0]<='6') and((classe[-1]>='A' and classe[-1]<='Z') or (classe[-1]>='a' and classe[-1]<='z')):
            return True
    else:
        return False   


def Classe(classe):
    classe=classe.strip(" ")
    correction=""
    if Valide_Classe(classe)==True:
        correction=str(classe[0])+"em"+classe[-1]
        return correction

def nettoyage_chaine(donnee):
    # Nettoyer la chaîne de données
    donnee = donnee.strip()  # Enlever les espaces au début et à la fin
    donnee = donnee.replace(" ", "")  # Enlever les espaces inutiles
    donnee = donnee.replace(",", ".")  # Remplacer les virgules par des points

    # Séparer les matières
    matieres = donnee.split("#")
    notes = {}

    for matiere in matieres:
        # Séparer le nom de la matière de ses notes
        name, note_en_chaine = matiere.split("[")
        note_en_chaine = note_en_chaine[:-1]  # Enlever le crochet fermant à la fin

        # Séparer les notes de devoir de la note d'examen
        note_devoirs, note_examen = note_en_chaine.split(":")
        note_devoirs = note_devoirs.split("|")

        # Convertir les notes en nombres
        notes[name] = [float(note) for note in note_devoirs]
        notes[name].append(float(note_examen))

    return notes

def calcul(donnee):
    # Nettoyer les notes
    notes = nettoyage_chaine(donnee)

    # Calculer la moyenne de chaque matière
    moyenne_matieres = []
    for matiere in notes:
        moy_matiere = sum(notes[matiere]) / len(notes[matiere])
        moyenne_matieres.append(moy_matiere)
    
    # Calculer la moyenne générale
    moy_generale = sum(moyenne_matieres) / len(moyenne_matieres)

    return moy_generale


# In[7]:




MOYENNE=[]
cpt,i=0,0
numero=[]
nom=[]
prenom=[]
Nouvelle_Date=[]
date=[]
DATE=[]
CLASSE=[]
X=[]
Correction_date=[]

with open(r"C:\Users\lenovo\Downloads\Nouveau dossier\monrepertoire\Donnees_Projet_Python_DataC5.csv") as f:
    for ligne in f:
        if cpt>=1:
            X=ligne.split(",")
            if not '' in X:
                
                    try:
                        # print(nettoyage_chaine(X[6]))
                        # print(i+1,"__",round(calcul(X[6]),2));i+=1
                        MOYENNE.append(round(calcul(X[6]),2))
                    except:
                        # print("Invalide !!")
                        X[3]=X[3].strip(" ").replace("Ã","é")
                    #print(X,"\n\n")
                        A=str(X[1])
                        if valide_num(A):
                            numero.append(A)
                        B=X[2]   
                        if Nom(B)==True:
                            nom.append(B)
                        C=X[3]
                        if Prenom(C)==True:
                            prenom.append(C);CLASSE.append(Classe(X[5]))    
                        X[4]=X[4].replace("-","/")
                        X[4]=X[4].replace("mars","3")  
                        X[4]=X[4].replace(" ","/")
                        X[4]=X[4].replace(":","/")
                        X[4]=X[4].replace(".","/")
                        X[4]=X[4].replace("|","/")
                        X[4]=X[4].replace("fev","2")
                        X[4]=X[4].replace("_","/")
                        X[4]=X[4].replace("decembre","12")
                        X[4]=X[4].replace(",","")
                        X[4]=X[4].replace('"',"")
                        X[4]=X[4].replace('Ã‡',"ai") 
                        X[4]=X[4].strip('////////////////////////')                   
                        date.append(X[4])
        cpt+=1           
for i in date:
    i=i.split('/')
    if len(i)==3:
        DATE.append(i)
#print(DATE)    
for j in DATE:
    #print("\n",j,"\n")
    if len(j[-1])==2:
        if j[-1]<='24':
            a=int(j[-1])+2000
            j[-1]=str(a)
        elif '24'<j[-1]<='99':
            b=int(j[-1])+1900
            j[-1]=str(b)
            
k=0 
#for i in TEST:
#    print("\n",k+1,i,"\n");k+=1                 
for i in DATE:
    val=Valide_date(int(i[0]),int(i[1]),int(i[2]))
    if val:
        #print(k+1," ",val);k+=1
        Nouvelle_Date.append(i)
        
k=0 
joindre=[]
for i in Nouvelle_Date:
    joins=i[0]+"/"+i[1]+"/"+i[2]
    joindre.append(joins)

Nouveau_Fichier=zip(numero,prenom,nom,CLASSE,joindre,MOYENNE)
TEST=list(Nouveau_Fichier)
#TEST=sorted(TEST)


# In[8]:


LISTE=[]
for i in range(len(TEST)):
        Dictionnaire={"Numero":TEST[i][0],"Nom":TEST[i][1],"Prenom":TEST[i][2],"Classe":TEST[i][3],"Date de naissance":TEST[i][4],"Moyenne générale":TEST[i][5]}
        LISTE.append(Dictionnaire)
             
            


# In[9]:


#  # Initialisation des listes d'informations valides et invalides
valides = []
invalides = []

# # Fonction pour vérifier la validité d'une information
def est_valide(info):
#     # Ici, on considère que l'information est valide si elle contient au moins 3 caractères
      return len(info) >= 3

# # Fonction pour ajouter une information
def ajouter_info(info):
    if est_valide(info):
            valides.append(info)
            print("L'information a été ajoutée avec succès.")
    else:
            invalides.append(info)
            print("L'information est invalide et a été ajoutée à la liste des informations invalides.")

# # Fonction pour modifier une information invalide
def modifier_info(invalide_num, nouvelle_info):
        if est_valide(nouvelle_info):
            invalides.pop(invalide_num - 1)
            valides.append(nouvelle_info)
            print("L'information a été modifiée avec succès et ajoutée à la liste des informations valides.")
        else:
            print("La nouvelle information est invalide. La modification a échoué.")

# # Fonction pour afficher une information par son numéro
def afficher_info(num):
    if valide_num(num):
        print("")
    else:
        num_invalide = num - len(valides)
        if num_invalide <= len(invalides):
              print(invalides[num_invalide - 1])
        else:
              print("Le numéro d'information est invalide.")

# # Fonction pour afficher les cinq premières informations
def afficher_premieres():
        print("Informations valides :")
        for i in range(min(5, len(valides))):
            print(f"{i + 1}. {valides[i]}")
        print("Informations invalides :")
        for i in range(min(5, len(invalides))):
            print(f"{i + 1}. {invalides[i]}")


# In[10]:



# Boucle principale du programme
while True:
    print("==========================")
    print("Menu ")
    print("==========================\n")
    print("\n1. Ajouter une information")
    print("=====================================")
    print("\n2. Modifier une information invalide")
    print("===========================================")
    print("\n3. Afficher une information par son numéro")
    print("===========================================")
    print("\n4. Afficher les cinq premières informations")
    print("===========================================")
    print("\n5. Quitter")
    print("============================")
    choix = input("Entrez votre choix : ")
    print("============================")
    if choix == "1":
        print("=============================")
        info = input("Entrez l'information à ajouter : ")
        print("=============================")
        ajouter_info(info)
    elif choix == "2":
        print("========================================")
        invalide_num = int(input("Entrez le numéro de l'information invalide à modifier : "))
        print("========================================")
        nouvelle_info = input("Entrez la nouvelle information : ")
        print("========================================")
        modifier_info(invalide_num, nouvelle_info)
    elif choix == "3":
        print("========================================")
        num = int(input("Entrez le numéro de l'information à afficher : "))
        print("========================================")
        afficher_info(num)
    elif choix == "4":
        # Affichage du tableau avec tabulate
        print(tabulate(LISTE, headers="keys", tablefmt="psql"))
        for i in range(len(LISTE)):
            print(i+1)
#        # afficher_premieres()
    elif choix == "5":
        break
    else:
        print("Choix invalide !!!!")






