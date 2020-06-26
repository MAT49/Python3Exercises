# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:35:57 2020

@author: Motoko
"""


from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())