#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = number * (-1)
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste = [0]*len(prefixes)
    for i in range(len(prefixes)):
        liste[i] = prefixes[i] + suffixe
    return liste


def prime_integer_summation() -> int:
    somme = 2
    c = 0
    i = 2
    while c < 100:
        i += 1
        a = True
        for j in range(2,i-1):
            if i%j == 0:
                a = False
                break
        if a == True:
            somme += i
            c += 1
    return somme


def factorial(number: int) -> int:
    factoriel = number
    while number != 1:
        number += -1
        factoriel = factoriel * number
    return factoriel


def use_continue() -> None:
    for i in range(1,10):
        if i == 5:
            continue
        else : print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    liste_bool = [True]*len(groups)
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            if groups[i][j] == 25:
                liste_bool[i] = True
                break
            elif groups[i][j] == 50:
                for k in range(len(groups[i])):
                    if groups[i][k] > 70:
                        liste_bool[i] = False
            elif groups[i][j] < 18:
                liste_bool[i] = False

        if len(groups[i]) > 10 or len(groups[i]) <= 3:
            liste_bool[i] = False

    return liste_bool


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
