# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:11:19 2023

@author: sondrevoll - 279507

Oppgave h) a)

Anta du har en plante som krever at temperaturen er +5 grader celsius for å vokse i det hele
tatt, og så vokser fortere desto varmere det er, lineært med temperatur over 5 grader. Skriv
en funksjon som regner ut summen av alle tall over 5 i lista. Så i lista [4, 7, 15] blir summen 0
(for 4) + 2 (for 7) + 10 (for 15).

a. Frivillig: Planten tar skade av minusgrader, så minusgrader gir «negativ vekst» og
planten dør hvis den når 0.

"""

liste1 = [-1, 4, 5, 7, 15, 27]


def varmevekst(lst):
    lengde = len(lst)
    
    for i in range(0, lengde):
        varme = lst[i] - 5
        
        if varme > 0:
            print(f"summen av tall {[i]} i lista er {varme}.")
        
        elif varme <= 0:
            print(f"Summen av tall {[i]} i lista er {varme} så planten dør")
    
varmevekst(liste1)
    