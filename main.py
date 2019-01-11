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
    frt,bck='',''
    def __init__(self, parent, *args, **kwargs):
        self.root=parent
        self.make={}
        parent.title("Flash Card")
        self.loadSet()
        self.frt,self.bck=self.serveCard()

        self.exitButton = tk.Button(parent, text="Exit", fg="red", command=quit)
        self.exitButton.place(x=10,y=10)

        self.flashData=tk.Label(parent,text=self.frt)
        self.flashData.pack()

        #note to self:
        #passing an arguement into nextFlashCard triggers the button press immediately
        #command takes a reference to a function, adding an arguement ends up calling the function
        #use lambda to create anonoymous function, cleanly fixes this problem
        self.nextButton = tk.Button(parent, text="Show Reverse",command=lambda:self.nextFlashCard(parent))
        self.nextButton.pack()



    def nextFlashCard(self,parent):
        print("button pressed")
        self.flashData.configure(text=self.bck)
        self.flashData.pack()

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
    root.geometry("300x200+30+30")
    myApp=FlashCardMain(root)
    root.mainloop()


