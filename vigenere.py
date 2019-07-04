def chiffrement_vigenere(L, C):
    """L: liste initiale (mot à chiffrer)
       C: clé de chiffrement (ensemble des décalages)"""
    M = []
    for k in range(len(L)):
        i = k % len(C)
        M.append((L[k] + C[i]) % 26)
    return M

def dechiffrement_vigenere(M, C):
    """M: liste à déchiffrer 
       C: clé de chiffrement"""
    L = []
    for i in range(len(M)):
        k = i % len(C)
        L.append((M[i] - C[k]) % 26)
    return L


def mot_devient_liste(mot, alphabet):
    L = []
    for lettre in mot:
        if lettre in alphabet:
            L.append(alphabet.index(lettre))
    return L

def liste_devient_mot(liste, alphabet):
    mot = ""
    for nombre in liste:
        mot += alphabet[nombre]
    return mot

# tests
alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    mot = input("Choisir le mot initial (uniquement en minuscules) à chiffrer : ")
    print("Vous avez choisi le mot :", mot)
    L = mot_devient_liste(mot, alphabet)
    print("Liste des indices des lettres de votre mot :", L)
    
    cle = input("Choisir la clé de chiffrement (uniquement en minuscules) : ")
    print("Vous avez choisi la clé :", cle)
    C = mot_devient_liste(cle, alphabet)
    print("Liste des indices des lettres de votre clé :", C)
    
    V = chiffrement_vigenere(L, C)
    print("Liste obtenue après chiffrement de Vigenère :", V)
    print("Mot obtenu après chiffrement de Vigenère :", end=" ")
    print(liste_devient_mot(V, alphabet))

    print("Vérification")
    L = dechiffrement_vigenere(V, C)
    print("Mot déchiffré :", liste_devient_mot(L, alphabet))

    continuer = input("Voulez-vous continuer ? (o/n) ")
    if continuer == "n" or continuer == "N":
        break
