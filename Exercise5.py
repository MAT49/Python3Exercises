# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:02:07 2020

@author: Motoko
"""


my_name = 'Zed'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

kilo = my_weight / 2.2
cm = my_height * 2.54

print(f"Le's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

print(f"{my_height} inches is {round(cm)}, and {my_weight} is {round(kilo)} kg.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")