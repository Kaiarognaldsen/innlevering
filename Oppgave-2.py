#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:20:23 2018

@author: kaiarognaldsen
"""
from numpy import sqrt

x = input("Skal du regne ut E, m eller v?")
if x == "E":
    m = int(input("Skriv verdien til m i kg."))
    v = int(input("Skriv verdien til v i m/s."))
    E = (0.5*m*v**2)
    print (E, 'joule')
    
elif x == 'm':
    E = int(input("Skriv verdien til E målt i joule."))
    v = int(input("Skriv verdien til v målt i m/s.")) 
    m = (E/(0.5*v**2))
    print(m, 'kg')

elif x == "v":
    E = int(input("Skriv verdien til E målt i joule."))
    m = int(input("Skriv verdien til m i kg."))
    v = sqrt(E/(0.5*m))
    print(v, 'm/s')
