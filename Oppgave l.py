# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:56:52 2023

@author: sondrevoll- 279507

Oppgave l

Bruk funksjonen fra oppgave h) for å finne total vekst for planten gitt lista med temperature
"""


liste1 = [-1, 4, 5, 7, 15, 27]
summen_av_vekst = 0


def varmevekst(lst, summen):
    lengde = len(lst)
    
    for i in range(0, lengde):
        varme = lst[i] - 5
        summen = summen + varme
        
    return summen

resultat = varmevekst(liste1, summen_av_vekst)
print(f"Den totale veksten av planten er {resultat}")