# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:11:19 2023

@author: sondrevoll - 279507

Oppgave h)

Anta du har en plante som krever at temperaturen er +5 grader celsius for å vokse i det hele
tatt, og så vokser fortere desto varmere det er, lineært med temperatur over 5 grader. Skriv
en funksjon som regner ut summen av alle tall over 5 i lista. Så i lista [4, 7, 15] blir summen 0
(for 4) + 2 (for 7) + 10 (for 15).

a. Frivillig: Planten tar skade av minusgrader, så minusgrader gir «negativ vekst» og
planten dør hvis den når 0.

b. Frivillig avansert DAT200 pensum: Skriv en funksjon som finner perioden i lista som
gir maksimal vekst samt summen for denne perioden. Funksjonen skal returnere alle
tre tallene. Dette er et eksempel på «maksimal delsekvens sum» problemet som
brukes for å illustrere effektive algoritmer i emnet DAT200.

"""


liste1 = [0, 4, 7, 15, 27]


def varmevekst(lst):
    lengde = len(lst)
    
    for i in range(0, lengde):
        varme = lst[i] - 5
        
        if varme >= 0:
            print(f"summen av tall {[i]} i lista er {varme}.")
        
        elif varme < 0:
            varme = 0
            print(f"Summen av tall {[i]} i lista er {varme}.")
    
varmevekst(liste1)
    