
A=["JANVIER","FEVRIER","MARS","AVRIL","MAI","JUIN","JUILLET","AOUT","SEPTEMBRE","OCTOBRE","NOVEMBRE","DECEMBRE"]
B=["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
max=len('JAnvier')
for i in A:
    if len(i)>max:
         max=len(i) 
for i in range(12):
     if max>len(A[i]):
          A[i]=A[i]+(" "*(max-len(A[i])))     
for i in B:
    if len(i)>max:
         max=len(i) 
for i in range(12):
     if max>len(B[i]):
          B[i]=B[i]+(" "*(max-len(B[i])))          
C=int(input("Tapez 1 pour afficher les mois en français, 2 pour les mois en anglais et 3 pour quitter : "))
while (C!=1 and C!=2 and C!=3):
  C=int(input("Vous avez fait une erreur !\nTapez 1 pour afficher les mois en français, 2 pour les mois en anglais et 3 pour quitter:"))
  print("\n")
if C==1 or C==2:
     
      if C==1:
           T=A
           print("Vous avez choisi d'afficher les mois en FRANÇAIS :")
      else:
           T=B     
           print("Vous avez choisi d'afficher les mois en ANGLAIS :")
      for i in range(0,10,3):
           print(end=" ")
           print(end=T[i]) 
      print("\n")  
      for i in range(1,11,3):
           print(end=" ")
           print(end=T[i]) 
      print("\n")
      for i in range(2,12,3):
           print(end=" " )
           print(end=T[i]) 
      print("\n") 

if (C==3):
    print("Vous avez choisi de quitter !")
    exit           
if (C!=1 and C!=2 and C!=3):
    print("Choix non pris en compte !")


