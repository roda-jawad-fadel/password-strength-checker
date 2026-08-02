#!/usr/bin/env python3
"""
Analyseur de robustesse des mots de passe — Entropie de Shannon.

Projet tutoré — Université Paris 8 (L3 Mathématiques, UE Théorie de
l'information) : "Analyse de la robustesse des mots de passe avec
l'entropie de Shannon".

Ce script calcule deux mesures complémentaires :

  - L'entropie théorique : H = L * log2(N), en supposant un mot de passe
    totalement aléatoire sur un alphabet de taille N.
  - L'entropie de Shannon (dite "réelle") : basée sur la fréquence effective
    des caractères présents dans le mot de passe analysé.

L'écart entre les deux illustre pourquoi un mot de passe "qui a l'air
compliqué" (ex: substitutions o->0, a->@) n'est pas forcément robuste :
la structure linguistique et les habitudes humaines réduisent
l'imprévisibilité réelle par rapport au modèle mathématique idéal.
"""

from collections import Counter
from math import log2


def detecter_taille_alphabet(mot_de_passe: str) -> int:
    """Estime la taille de l'alphabet utilisé à partir de la composition du mot de passe."""
    taille = 0
    if any(c.islower() for c in mot_de_passe):
        taille += 26
    if any(c.isupper() for c in mot_de_passe):
        taille += 26
    if any(c.isdigit() for c in mot_de_passe):
        taille += 10
    if any(not c.isalnum() for c in mot_de_passe):
        taille += 33  # approximation des caractères spéciaux courants
    return max(taille, 1)


def entropie_theorique(longueur: int, taille_alphabet: int) -> float:
    """Entropie en supposant un mot de passe aléatoire uniforme : H = L * log2(N)."""
    return longueur * log2(taille_alphabet)


def entropie_shannon(mot_de_passe: str) -> float:
    """Entropie réelle basée sur la fréquence des caractères observés."""
    occurrences = Counter(mot_de_passe)
    longueur = len(mot_de_passe)
    entropie_par_caractere = 0.0
    for nombre in occurrences.values():
        probabilite = nombre / longueur
        entropie_par_caractere -= probabilite * log2(probabilite)
    return entropie_par_caractere * longueur


def temps_de_cassage(bits_entropie: float, tentatives_par_seconde: float = 1e9) -> str:
    """Estime un temps de cassage moyen (attaque par force brute)."""
    nombre_possibilites = 2 ** bits_entropie
    secondes = nombre_possibilites / (2 * tentatives_par_seconde)
    annees = secondes / (3.15e7)
    if annees < 1:
        return f"{secondes:.2f} secondes"
    return f"{annees:.2e} années"


def analyser(mot_de_passe: str):
    longueur = len(mot_de_passe)
    taille_alphabet = detecter_taille_alphabet(mot_de_passe)

    h_theorique = entropie_theorique(longueur, taille_alphabet)
    h_shannon = entropie_shannon(mot_de_passe)

    print(f"Mot de passe analysé : {mot_de_passe}")
    print(f"Longueur             : {longueur}")
    print(f"Alphabet estimé       : {taille_alphabet} caractères possibles")
    print(f"Entropie théorique    : {h_theorique:.2f} bits")
    print(f"Entropie de Shannon   : {h_shannon:.2f} bits (basée sur les caractères réellement utilisés)")
    print(f"Temps de cassage estimé (théorique) : {temps_de_cassage(h_theorique)}")

    if h_theorique < 40:
        niveau = "Faible"
    elif h_theorique < 70:
        niveau = "Moyen"
    elif h_theorique < 90:
        niveau = "Bon"
    else:
        niveau = "Excellent"
    print(f"Niveau de robustesse (estimation) : {niveau}")


def main():
    mot_de_passe = input("Mot de passe à analyser : ")
    print()
    analyser(mot_de_passe)


if __name__ == "__main__":
    main()
