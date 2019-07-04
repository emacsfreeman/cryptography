# -*- coding: utf-8 -*-

# ce programme élimine la ponctuation et les espaces dans un texte

text_choice = input("Avez-vous un fichier de texte à formater ? (o/n) ")
if text_choice == "o" or text_choice == "O":
    filename = input("Nom du fichier texte : ")
    fichier = open(filename, 'r')
    texte = fichier.read()
    fichier.close()
else:
    texte = "Ceci n'est qu'un exemple"
    
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nbcar = len(texte)
print("Texte :\n", texte)
print("Nombre de caractères : ", nbcar)
texteformate = ""
for k in range(nbcar):
    j = 0
    trouve = 0
    while (j < len(alphabet)) and (trouve == 0):
        if texte[k] == alphabet[j]:
            trouve = 1
        if trouve == 0:
            j += 1
            if trouve == 1:
                texteformate = texteformate+texte[k]
print(texteformate)
