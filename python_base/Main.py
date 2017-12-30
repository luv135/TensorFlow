#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'LuoWei'

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, World.')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='quit', command=self.quit)
        self.quitButton.pack()


app = Application()
app.master.title('Hello World')

app.mainloop()