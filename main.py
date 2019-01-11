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
import tkinter as tk

fileName="testset.txt"


class FlashCardMain(object):
    pairs={}
    def __init__(self, parent, *args, **kwargs):
        self.root=parent
        self.make={}
        parent.title("Flash Card")
        self.loadSet()
        frt,bck=self.serveCard()

        self.label=tk.Label(parent,text=frt)
        self.label.pack()

    def serveCard(self):
        frontSide = choice(list(self.pairs))
        backSide = self.pairs[frontSide]
        return frontSide, backSide

    def loadSet(self):
        try:
            # file=open(fileName,"r")
            file = codecs.open(fileName, encoding='utf-8')
        except:
            print("Error: opening file")
        for i, line in enumerate(file):
            eng, jpn = line.split(":")
            self.pairs[eng] = jpn

if __name__ == "__main__":
    root=tk.Tk()
    root.geometry("300x200")
    myApp=FlashCardMain(root)
    root.mainloop()



