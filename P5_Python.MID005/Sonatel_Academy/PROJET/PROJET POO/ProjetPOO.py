# -*- coding: utf-8 -*-
"""

@author: Ibrahima Gabar Diop
"""

import re
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
        return True
def nettoyage_chaine(note):
    # Nettoyer la chaîne de données
    note = note.strip()  # Enlever les espaces au début et à la fin
    note = note.replace(" ", "")  # Enlever les espaces inutiles
    note = note.replace(",", ".")  # Remplacer les virgules par des points
    # Séparer les matières
    matieres = note.split("#")
    notes = {}

    for matiere in matieres:
        # Séparer le nom de la matière de ses notes
        nom_MATIERE, note_en_chaine = matiere.split("[")
        note_en_chaine = note_en_chaine[:-1]  # Enlever le crochet fermant à la fin

        # Séparer les notes de devoir de la note d'examen
        if len(note_en_chaine.split(":"))==2:
            note_devoirs, note_examen = note_en_chaine.split(":")
            note_devoirs = note_devoirs.split("|")
        else:
            note_devoirs=note_en_chaine
            note_devoirs = note_devoirs.split("|")
        # Convertir les notes en nombres
        notes[nom_MATIERE] = [float(note) for note in note_devoirs]
        notes[nom_MATIERE].append(float(note_examen))

    return notes
class etudiant:
  def __init__(self,numero,prenom,nom,classe,date):
    self.prenom=prenom
    self.nom=nom
    self.numero=numero
    self.classe=classe
    self.date=date
  def valid_num(self):
    if isinstance(self.numero, str):
            return re.match(r'^[A-Z0-9]{7}$', self.numero) is not None
    else:
            return False
        
  def valid_prenom(self):
    return re.match(r'^[A-Za-z" "]{3,}$', self.prenom) is not None

  def valid_nom(self):
        return re.match(r'^[A-Za-z" "]{2,}$', self.nom) is not None
    
  def valid_classe(self):
      return re.match(r'^[3-6][a-z" "]*[A-Z]$', self.classe) is not None 
  
  def correcton_classe(self):
     return str(self.classe[0])+"em"+self.classe[-1]
 
  def correction_date(self):
    self.date=self.date.replace("-","/")
    self.date=self.date.replace("mars","3")  
    self.date=self.date.replace(" ","/")
    self.date=self.date.replace(":","/")
    self.date=self.date.replace(".","/")
    self.date=self.date.replace("|","/")
    self.date=self.date.replace("fev","2")
    self.date=self.date.replace("_","/")
    self.date=self.date.replace("decembre","12")
    self.date=self.date.replace(",","")
    self.date=self.date.replace('"',"")
    self.date=self.date.replace('Ã‡',"ai") 
    self.date=self.date.strip('////////////////////////')                     
    Date=self.date.split('/')
    if len(Date)==3:
          if len(Date[-1])==2:
            if Date[-1]<='24':
                a=int(Date[-1])+2000
                Date[-1]=str(a)
            elif '24'<Date[-1]<='99':
                b=int(Date[-1])+1900
                Date[-1]=str(b)    
    val=Valide_date(int(Date[0]),int(Date[1]),int(Date[2]))
    if val:
      return True 
    return False                  

class Notes:
  def __init__(self,note):
    self.note=note

  def calcul(self):
      # Nettoyer les notes
      notes = nettoyage_chaine(self.note)
      # Calculer la moyenne de chaque matière
      moyenne_matieres = []
      for matiere in notes:
          moy_matiere = sum(notes[matiere]) / len(notes[matiere])
          moyenne_matieres.append(round(moy_matiere,2))
      
      # Calculer la moyenne générale
      moy_generale = sum(moyenne_matieres) / len(moyenne_matieres)
      moy_eleve={"Moyenne Genereale":float(round(moy_generale))}
      moyenne_matieres.append(moy_eleve)
      return moyenne_matieres

liste_valide=[]  
liste_invalide=[]  
cpt=0
import csv
with open(r"C:\Users\lenovo\Downloads\Nouveau dossier\monrepertoire\Donnees_Projet_Python_DataC5.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    #print(list(reader))
    print("")
    for row in reader:
        new_row=row[0].split(',')
        
        if not '' in row:
            try:
                numero, nom, prenom, classe, date_naissance, notes = new_row[1],new_row[2],new_row[3],new_row[4],new_row[5],new_row[6]
                Gabar = etudiant(numero, prenom, nom, date_naissance, classe)
                Note_Gabar=Notes(notes)
                #print(Note_Gabar.calcul())
                #Gabar=etudiant("AE313BR","Ibrahima Gabar","Diop","6em B","29/08/1998","18,57")   
                
                if (Gabar.valid_num()) and (Gabar.valid_prenom()) and (Gabar.valid_nom()) and (Gabar.valid_classe() and Gabar.correction_date()):
                    Gabar.classe=Gabar.correcton_classe()
                    etudiant_valide={"numero":Gabar.numero,"prenom":Gabar.prenom,"nom":Gabar.nom,"classe":Gabar.classe,"date_naissance":Gabar.date,"note":Note_Gabar.calcul()}
                    liste_valide.append(etudiant_valide)
                    print(cpt+1,etudiant_valide);cpt+=1
                    
                else:
                    etudiant_invalide={"numero":Gabar.numero,"prenom":Gabar.prenom,"nom":Gabar.nom,"classe":Gabar.classe,"date_naissance":Gabar.date,"note":Note_Gabar.calcul()}
                    liste_invalide.append(etudiant_invalide)
                    #print(cpt+1,etudiant_invalide);cpt+=1
            except:
                x=0



