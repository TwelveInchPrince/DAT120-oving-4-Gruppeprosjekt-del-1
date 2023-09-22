# -*- coding: utf-8 -*-
"""
@author: sondrevoll - 279507

Oppgave e)

Skriv en funksjon som tar inn ei liste med tall. For hvert tall i lista unntatt det siste skal
funksjonen regne ut differansen mellom neste tall i lista og dette tallet. Differansene skal
legges inn i ei ny liste.
"""

liste1 = [1, 3, 6, 10]
liste2 = []


def differansen(lst):
    lengde= len(liste1) 
    for i in range(1, lengde):
        diff= lst[i] - lst[i-1]
        liste2.append(diff)
   
        
differansen(liste1)

print(liste2)