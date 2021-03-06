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
from tkinter import messagebox

class FlashCardMain(object):
    pairs={}
    frt,bck='',''
    cardSide=False
    dirname="Cardsets"
    packs=["Genki 1 Greetings",
           "Genki 1 Lesson 1",
           "Genki 1 Lesson 2",
           "error_trigger"]
    fileName = "Genki 1 Greetings.txt"
    def __init__(self, parent, *args, **kwargs):
        self.root=parent
        self.make={}
        parent.title("Flash Card")
        self.loadSet()
        self.frt, self.bck = self.serveCard()
        self.tkvar = tk.StringVar()
        self.tkvar.set("Genki 1 Greetings")
        self.front_color = "light grey"
        self.back_color = "white"
        self.runApplication(parent)
        
    def runApplication(self,parent):
        #Create a popup menu and decide what happens if it get's changed
        popupMenu = tk.OptionMenu(parent, self.tkvar, *self.packs)
        tk.Label(parent, text="Flash Set").place(x=250,y=13,height=25)
        popupMenu.place(x=300,y=10)
        self.tkvar.trace('w', self.change_dropdown)

        #Exit Button
        self.exitButton = tk.Button(parent, text="Exit", fg="red", command=quit)
        self.exitButton.place(x=10,y=10)

        #Card Area
        self.cardArea=tk.Frame(parent,
                               bd=1,
                               relief=tk.RAISED,
                               height=100,
                               width=300,
                               bg="white")
        self.cardArea.place(x=125,y=75)

        #The 'face' of the flash card
        self.flashData=tk.Label(parent,text=self.bck,bg=self.back_color)
        self.flashData.config(font=("courier",10))
        self.flashData.place(x=150,y=100)

        #note to self:
        #passing an arguement into nextFlashCard triggers the button press immediately
        #command takes a reference to a function, adding an arguement ends up calling the function
        #use lambda to create anonoymous function, cleanly fixes this problem
        self.nextButton = tk.Button(parent, text="Flip Card",command=lambda:self.flipFlashCard())
        self.nextButton.place(x=10,y=100)

        self.shuffleCard = tk.Button(parent, text="Random Card",command=lambda:self.changeCard())
        self.shuffleCard.place(x=10, y=140)

    def change_dropdown(self,*args):
        print(self.tkvar.get())
        self.fileName = self.tkvar.get()+".txt"
        self.loadSet()
        self.changeCard()

    def flipFlashCard(self):
        #print("button pressed")
        if(self.cardSide):
            self.flashData.configure(text=self.bck,bg=self.back_color)
            self.cardArea['bg']=self.back_color
        else:
            self.flashData.configure(text=self.frt,bg=self.front_color)
            self.cardArea['bg']=self.front_color
        self.cardSide=not self.cardSide
        self.flashData.place(x=150,y=100)

    def changeCard(self):
        self.frt,self.bck=self.serveCard()
        self.flashData.configure(text=self.bck,bg=self.back_color)
        self.cardArea['bg']=self.back_color
        self.cardSide=False

    def serveCard(self):
        frontSide = choice(list(self.pairs))
        backSide = self.pairs[frontSide]
        return frontSide, backSide

    def loadSet(self):
        #print("loading set")
        try:
            # file=open(fileName,"r")
            file = codecs.open(os.path.join(self.dirname,self.fileName), encoding='utf-8')
            self.pairs.clear()
            for i, line in enumerate(file):
                eng, jpn = line.split(":")
                self.pairs[eng] = jpn
        except:
            print("Error: opening file")
            messagebox.showerror("Error","File not found")

if __name__ == "__main__":
    root=tk.Tk()
    root.geometry("450x200+30+30")
    myApp=FlashCardMain(root)
    root.mainloop()


