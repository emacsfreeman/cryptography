# -*- coding: utf-8 -*-

# ce programme met un texte formaté en minuscules

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
texteformate = ""
for k in range(nbcar):
    if ord(texte[k]) < 97:
        texteformate += chr(ord(texte[k]) + 32)
    else:
        texteformate += texte[k]
print(texteformate)
