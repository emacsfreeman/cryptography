# -*- coding: utf-8 -*-

# ce programme affiche la fréquence d'apparition de la lettre demandée
# par l'utilisateur dans un texte préalablement formatté (caractères
# mis en minuscules, espaces et signes de ponctuation supprimés)

text_choice = input("Avez-vous un fichier de texte à formater ? (o/n) ")
if text_choice == "o" or text_choice == "O":
    filename = input("Nom du fichier texte : ")
    fichier = open(filename, 'r')
    texte = fichier.read()
    fichier.close()
else:
    texte = "CeciNEstQuUnexemple"

    
nbcar = len(texte)
print("Texte :\n", texte)
print("Nombre de caractères :", nbcar)
lettre = input("Lettre : ")
compteur = 0
for k in range(nbcar):
    if texte[k] == lettre:
        compteur += 1
freq = compteur/nbcar
print("Fréquence :", freq)
