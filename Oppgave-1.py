#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:38:56 2018

@author: kaiarognaldsen
"""

import math

ioner = float(input("Hvor mange ioner per mol er det i løsningen din?"))

pH = -math.log(ioner) 

if 0 <= pH < 7:
    print("Løsningen er sur.")
elif pH == 7:
    print("Løsningen er nøytral")
else:
    print("Løsningen er basisk")
    