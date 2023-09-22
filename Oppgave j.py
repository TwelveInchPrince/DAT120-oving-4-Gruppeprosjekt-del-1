# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:46:55 2023

@author: Sondre_Voll- 279507

Oppgave j

Bruk funksjonen fra oppgave e) til å finne ut om temperaturen er stigende eller synkende for
hvert tidspunkt. Gå gjennom lista som dere får når dere kaller funksjonen fra oppgave e) på
temperaturlista. For hvert element skriv ut indeksen og skriv ut «stigende» om differansen er
over 0, «synkende» om den er negativ eller «uforandret» om den er 0.
"""

liste1 = [1, 1, 3, 2, 6, 10, 7]
liste2 = []


def differansen(lst):
    lengde= len(liste1) 
    for i in range(1, lengde):
        diff= lst[i] - lst[i-1]
        liste2.append(diff)
        if diff > 0:
            print(f"tall {[i]} til {[i+1]} i lista har en vekst på {diff} og stigende.")    
   
        if diff < 0:
            print(f"tall {[i]} til {[i+1]}  i lista har en nedgang på {diff} og synkende.")    

        if diff == 0:
            print(f"tall {[i]} til {[i+1]}  i lista har en endring på {diff} og har null vekst.")    

        
differansen(liste1)

print(liste2)