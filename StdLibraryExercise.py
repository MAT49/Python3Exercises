# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:04:17 2020

@author: Motoko
"""


from os import getcwd, environ
import sys
import os


current = getcwd()
# print(current)
print(sys.platform)

print(os.environ)
print(os.getenv('HOME'))

# print(os.getenv('HOME'))