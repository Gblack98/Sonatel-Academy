def filtre_phrase(text):
    A=['.','!','?']
    phrase_filtrée=[]
    for i in text:
        if len(i)>=25 and (i[0]>='A' and i[0]<='Z' ) and (i[-1] in A):
            phrase_filtrée.append(i)
    return phrase_filtrée

texte=input(" Entrez votre text :").split(',')
phrase_filtrée=filtre_phrase(texte)
print("Phrase filtrée :",phrase_filtrée) 
