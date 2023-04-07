library(readr)
data<- read_csv("GitHub/Projet/P5-SONATEL-ACADEMY-DEV.DATA/P5_Python.MID005/Sonatel_Academy/PROJET/Donnees_Projet_Python_DataC5.csv")
Valide_donnee<-list()
Invalide_donne<-list()
ValeursNA <- which(is.na(data),arr.ind=TRUE)[,1]
data_sans_NA<-data[-ValeursNA,]
for(i in 1:nrow(data_sans_NA))
    {if (grepl("^[A-Z0-9]{7}$", data_sans_NA$Numero[i])&&
          grepl("^[A-Za-z]{3,}$", data_sans_NA$Prenom[i])&& 
          grepl("^[A-Za-z]{2,}$", data_sans_NA$Nom[i])&&
          grepl("^[0-9]{1,2}[A-Za-z]{2}$", data_sans_NA$Classe[i])){
              info<-list(numero=data_sans_NA$Numero[i], 
              prenom=data_sans_NA$Prenom[i],
              nom=data_sans_NA$Nom[i], 
              classe=data_sans_NA$Classe[i],
              date=data_sans_NA$Date_de_naissance[i])
              Valide_donnee[[i]]<-info
    }else{
          Invalide_donne[[i]]<-data[i,]
          } 
}
# Extraction des notes pour chaque matière
notes <- regmatches(data_sans_NA$note, gregexpr("\\[.+?\\]", data_sans_NA$note))

# Calcul de la moyenne pour chaque matière
moyennes <- list()
for (i in 1:length(notes)) {
  
  # Séparation des notes de devoir et de la note d'examen
  examen <- as.numeric(sub(":.*", "", notes[[i]]))
  devoirs <- as.numeric(strsplit(sub(".*:", "", notes[[i]]
  }