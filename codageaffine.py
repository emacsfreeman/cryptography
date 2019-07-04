# -*- coding: utf-8 -*-

# ce programme est un exemple de chiffrement par substitution
# il chiffre un texte préformatté en utilisant un cryptage affine
# donné par la fonction f(x) = mx + p
# pour des raisons d'efficacité il est préférable que m soit premier avec 26


def text_to_format():
    text_choice = input("Avez-vous un fichier de texte à formater ? (o/n) ")
    if text_choice == "o" or text_choice == "O":
        filename = input("Nom du fichier texte : ")
        fichier = open(filename, 'r')
        texte = fichier.read()
        fichier.close()
        return texte
    else:
        texte = "cecinestquunexemple"
        return texte


def code_text(m, p, texte):
    textecode = ""
    nbcar = len(texte)
    for k in range(nbcar):
        u = ord(texte[k]) - 97
        v = m * u + p
        w = v % 26
        t = chr(97 + w)
        textecode += t
    return textecode


def modulo_symetrics(modulo):
    compteur = 0
    I = [] # ligne
    J = [] # colonne (inverse)
    for i in range(1, modulo):
        for j in range(1, modulo):
            if i * j % modulo == 1:
                compteur += 1
                I.append(i)
                J.append(j)
    return I, J


# tests
while True:
    modulo = int(input("Taille de l'alphabet : "))
    ligne, colonne = modulo_symetrics(modulo)
    print("Liste des nombres inversibles modulo", modulo, " :\n", ligne)
    
    print("Paramètres du codage affine f(x) = mx + p")
    m = int(input("m = "))
    p = int(input("p = "))
    
    texte = text_to_format()
    print("Texte initial :", texte)
    
    textecode = code_text(m, p, texte)
    print("Texte codé    :", textecode)
    
    decodage = input("Voulez-vous décoder le texte ? (o/n) ")
    if decodage == "o" or decodage == "O":
        if m in ligne:
            m = colonne[ligne.index(m)] # on récupère l'inverse de m modulo taille de l'alphabet
            p = m * (modulo - p) % modulo
            textedecode = code_text(m, p, textecode)
            print("Texte décodé  :", textedecode)
        else:
            print("Impossible de déchiffrer avec les paramètres ({m}, {p}) sélectionnés car {m} n'a pas d'inverse modulo {modulo}.".format(m = m, p = p, modulo = modulo))
    continuer = input("Voulez-vous continuer ? (o/n) ")
    if continuer == "n" or continuer == "N":
        break

