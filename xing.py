#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from tkinter import  *
import  tkinter.messagebox as mb

class App:
    def __init__(self,master):
        b=Button(master,text='press me',command=self.info).pack()
    def info(self):
        mb.showinfo('information',"please don't press that button again!")

root=TK()
app=App(root)
root.mainloop()