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

fileName="testset.txt"

try:
    #file=open(fileName,"r")
    file=codecs.open(fileName, encoding='utf-8')
except:
    print("Error: opening file")

for line in file:
    print(repr(line))

