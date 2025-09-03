# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 11:44:08 2025

@author: mugee
"""

#methods -> functions of datatypes
#print("value".upper())
#print("VALUE".lower()) 
#print("VALUES".replace('S', '5'))   

#new functions
#print(abs(-5))
#print(max(10, 5))
#print(min(20, 10))
#print(len("Hellothere"))

#pythogorus theorem

#Ask user for width and height
width = int(input("Enter the width of the triangle: "))
heigth = int(input("Enter the height of the triangle: "))

#Calculate the hypotenus using the pythogorus theorem
hypotenus = (width**2 + heigth**2)**(1/2)

print()
#Output result
print("The length of the hypotenus is:", round(hypotenus,2))