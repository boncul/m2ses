#!/usr/bin/env python
#-*-coding:utf-8-*-
from Tkinter import *
pencere = Tk()
pencere.title("M2SES")

pgen = 300
pyuks = 300
ekrangen = pencere.winfo_screenwidth()
ekranyuks = pencere.winfo_screenheight()
x = (ekrangen - pgen) / 2
y = (ekranyuks - pyuks) / 2
pencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))

pencere.tk_setPalette("#D0A9F5")
etiket = Label(text = "SESLENDİRİLECEK CÜMLEYİ GİRİNİZ")
etiket.pack()
giris = Entry()
giris.pack()
def kaydet():
    
    veri = giris.get()
    veri = unicode.encode(unicode(veri),"utf8")
    cal(veri)
    
giris.delete(0,END)

dugme = Button(text = "Seslendir",command = kaydet )
dugme.pack()
dugme = Button(text = "cık",command = pencere.quit )

dugme.pack()
