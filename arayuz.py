#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
import Tkinter,tkFileDialog
pencere = Tkinter.Tk()
#pencere = Tk()
        
pencere.title("M2SES")

pgen = 300
pyuks = 300
ekrangen = pencere.winfo_screenwidth()
ekranyuks = pencere.winfo_screenheight()
x = (ekrangen - pgen) / 2
y = (ekranyuks - pyuks) / 2
pencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))

pencere.tk_setPalette("#D0A9F5")
etiket = Label(text="SESLENDİRİLECEK CÜMLEYİ GİRİNİZ")
etiket.pack()
giris = Entry(width = 50)
giris.pack()

def dosya_al():
    file = tkFileDialog.askopenfile(parent=pencere,mode='rb',title='Choose a file')
    if file != None:
        global veri
        veri = file.read()
        file.close()
        cal(veri)

def girdi_al():
    global veri
    veri = giris.get()
    veri = unicode.encode(unicode(veri),"utf8")
    cal(veri)

#def seslendir():
#    cal(veri)

giris.delete(0,END)

dugme = Button(text="Dosyadan Oku",command=dosya_al )
dugme.pack()
dugme = Button(text="Girdiden Oku",command=girdi_al )
dugme.pack()
#dugme = Button(text="Seslendir",command=seslendir )
#dugme.pack()
dugme = Button(text="Çık",command=pencere.quit )
dugme.pack()
