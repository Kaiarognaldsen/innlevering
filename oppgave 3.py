#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:20:28 2018

@author: kaiarognaldsen
"""
def biooppg():
    bnåværende = int(input("Hvor mange dyr er det for tiden?"))
    t = int(input("Hvor mange år skjer populasjonsendringen over?"))
    pa = input("Stiger populasjonen? ja / nei?")
    if pa == "ja":
        p = float(input("Hvor mange prosent stiger populasjonen per år?"))
        bny = (bnåværende * (1 +(p/100))**t)
        print("Det er {:.0f} dyr etter {} år.".format(bny, t))
    elif pa == "nei":
        p = float(input("Hvor mange prosent synker populsjonen?"))
        bny = (bnåværende * (1 -(p/100))**t)
        print("Det er {:.0f} dyr etter {} år.".format(bny, t))
    else:
        print("Ikke gyldig svar!")
        
print("Svaret er",biooppg())
    

