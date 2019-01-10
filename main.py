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
from tkinter import *

fileName="testset.txt"

def serveCard(pairs):
    frontSide=choice(list(pairs))
    backSide=pairs[frontSide]
    return frontSide,backSide


try:
    #file=open(fileName,"r")
    file=codecs.open(fileName, encoding='utf-8')
except:
    print("Error: opening file")

pairs={}
for i,line in enumerate(file):
    eng,jpn=line.split(":")
    pairs[eng]=jpn

for j in range(1):
    serveCard(pairs)

window = Tk()
window.title("Flash Cards")
window.geometry('300x250')
frt,bck=serveCard(pairs)
lbl=Label(window,text=frt)
lbl.grid(column=0,row=0)
def clicked():
    lbl.configure(text=bck)
btn = Button(window, text="See Answer", bg="white", fg="Black",command=clicked)
btn.grid(column=1, row=0)
window.mainloop()

#practice stuff
'''
if __name__ == "__main__":
    import timeit
    setup = "from __main__ import serveCard"
    print(timeit.timeit("serveCard()",setup=setup))
'''


