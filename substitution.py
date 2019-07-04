# -*- coding: utf-8 -*-

# ce programme affiche la fréquence d'apparition de toutes les lettres
# dans un texte préalablement formatté (caractères mis en minuscules,
# espaces et signes de ponctuation supprimés)

text_choice = input("Avez-vous un fichier de texte à formater ? (o/n) ")
if text_choice == "o" or text_choice == "O":
    filename = input("Nom du fichier texte : ")
    fichier = open(filename, 'r')
    texte = fichier.read()
    fichier.close()
else:
    texte = "cecinestquunexemple"

lettre1 = input("Lettre à substituer : ")
lettre2 = input("Lettre de substitution : ")
nbcar = len(texte)
print("Texte à coder : " + texte)
textecode = ""
for k in range(nbcar):
    if texte[k] == lettre1:
        textecode += lettre2
    else:
        textecode += texte[k]
print("Texte codé : " + textecode)
