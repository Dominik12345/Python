# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:31:51 2017

@author: kahl
"""

import json
import filterpy as fp

# How to write and read 
'''

g = open("TestFile.txt",'r+')
temp = "Hello World! \n Dies ist ein Testsatz."



g.write(temp)

g.close()


g = open("TestFile.txt",'r')

temp = g.read()

print("temp = ")
print(temp)

g.close()
'''


f = open("C:/Users/kahl/Documents/Data/review_observation_json.txt",'r')

temp = f.read()

print("temp = " + str(temp) )

f.close()

temp2 = json.loads(temp)

print(temp2)