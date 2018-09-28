#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:17:41 2018

@author: kaiarognaldsen
"""

n = float(input("Skriv inn N-fakultetet: "))
if n%1 != 0 or n < 0:
    print("Ikke gyldig!")
else:
    def r1matte(n):
        if n == 0:
            return 1
        else: 
            return n*r1matte(n-1)
    print ("Svaret er ", r1matte(n))
    
    
  

    
    
