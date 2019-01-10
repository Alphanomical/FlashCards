#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Filename: main.py
Author: Amit Anand
Contact: amit.anand@alumni.ubc.ca
Date Created: Jan 9, 2018
License: GNU General Public License v3.0
'''

import os
import codecs
from random import choice
from timeit import default_timer as timer

fileName="testset.txt"

def serveCard(pairs):
    frontSide=choice(list(pairs))
    backSide=pairs[frontSide]
    print(frontSide)
    input("Press Enter to see reverse")
    print(backSide)

try:
    #file=open(fileName,"r")
    file=codecs.open(fileName, encoding='utf-8')
except:
    print("Error: opening file")

pairs={}
for i,line in enumerate(file):
    eng,jpn=line.split(":")
    pairs[eng]=jpn

for j in range(10):
    serveCard(pairs)

#practice stuff
'''
if __name__ == "__main__":
    import timeit
    setup = "from __main__ import serveCard"
    print(timeit.timeit("serveCard()",setup=setup))
'''


