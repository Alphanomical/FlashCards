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
    cardSide=True
    packs={"testset.txt","testset2.txt"}

    def __init__(self, parent, *args, **kwargs):
        self.root=parent
        self.make={}
        parent.title("Flash Card")
        self.loadSet()
        self.nextCard()
        self.tkvar = tk.StringVar()
        self.tkvar.set("testset.txt")

        #Create a popup menu and decide what happens if it get's changed
        popupMenu = tk.OptionMenu(parent, self.tkvar, *self.packs)
        tk.Label(parent, text="Flash Set").place(x=125,y=15,height=25)
        popupMenu.place(x=175,y=10)
        self.tkvar.trace('w', self.change_dropdown)

        self.exitButton = tk.Button(parent, text="Exit", fg="red", command=quit)
        self.exitButton.place(x=10,y=10)

        self.flashData=tk.Label(parent,text=self.frt)
        self.flashData.place(x=150,y=100)

        #note to self:
        #passing an arguement into nextFlashCard triggers the button press immediately
        #command takes a reference to a function, adding an arguement ends up calling the function
        #use lambda to create anonoymous function, cleanly fixes this problem
        self.nextButton = tk.Button(parent, text="Flip Card",command=lambda:self.flipFlashCard(parent))
        self.nextButton.place(x=10,y=100)

    def change_dropdown(self,*args):
        print(self.tkvar.get())

    def nextCard(self):
        self.frt, self.bck = self.serveCard()

    def flipFlashCard(self,parent):
        print("button pressed")
        if(self.cardSide):
            self.flashData.configure(text=self.bck)
        else:
            self.flashData.configure(text=self.frt)
        self.cardSide=not self.cardSide
        self.flashData.place(x=150,y=100)

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


