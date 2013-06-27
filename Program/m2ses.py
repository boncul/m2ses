#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter,tkFileDialog
from Tkinter import *

import os
import sys
import time
import re

def kucukHarfCevir(sStr):
    str      = sStr
    aranan   = ''
    HARFDIZI = [
                ('İ','i'), ('Ğ','ğ'),('Ü','ü'), ('Ş','ş'), ('Ö','ö'),('Ç','ç'),
                ('I','ı')
               ]

    for aranan, harf in HARFDIZI:
        str = str.replace(aranan, harf)
        str = str.lower()

    return str

def lowercase(ch):
    return {
    'İ':u'i',
    'I':u'ı',
    'Ç':u'ç',
    'Ğ':u'ğ',
    'Ş':u'ş'   
    }.get(ch, ch.lower())
       
def sesli(ch):
    ch = lowercase(ch)
    if ch in [u'a', u'e', u'i', u'ı', u'o', u'ö', u'u', u'ü']:
        return True
    else:
        return False

#sesli=[u'a', u'e', u'i', u'ı', u'o', u'ö', u'u', u'ü']
hece =list()

def hecele(str):
    
    index=0
    length=len(str)
    while sesli(str[index]) == False  and length>index+1:
        index=index+1
    global hece
    try:
        if sesli(str[index+1]) :
            hece.append(str[0:index+1])
            #print str[0:index+1]
            hecele(str[index+1:])
        elif length>index+2:
            if sesli(str[index+2]):
                hece.append(str[0:index+1])
                #print str[0:index+1]
                hecele(str[index+1:])
            elif length>index+3:
                if sesli(str[index+3]) :
                    hece.append(str[0:index+2])
                    #print str[0:index+2]
                    hecele(str[index+2:])
                else:
                    if str[index+1:index+4] in [u'str', u'ktr', u'mtr', u'nsp']:
                        #print "istisna!.."
                        hece.append(str[0:index+2])
                        #print str[0:index+2]
                        hecele(str[index+2:])
                    else:
                        #print "üç sessiz, normal kural"
                        hece.append(str[0:index+3])
                        #print str[0:index+3]
                        hecele(str[index+3:])
            else:
                 hece.append(str)
                #print unicode(str)
        else:
            hece.append(str)
            #print unicode(str)
    except:
        hece.append(str)
        #print unicode(str)


def harfle(kelime):
    #kelime = kucukHarfCevir(ke
    harfler = list()

    for i in range(len(kelime)):
        harfler.append(kelime[i])

    return harfler

def islem_yapan(cumle):
    cumle = kucukHarfCevir(cumle)
    cumle = unicode(cumle, 'utf8')
    cumle = cumle.strip('."\',;')
    kelimeler = cumle.split()
    #hece_son = list()
    harf_son = list()
    for word in kelimeler:
        hecele(word)
        yeni_hece= list()
        
        for i in hece:
            yeni_hece.append(i)  
        for i in range(len(hece)):
            hece.pop()
        denge = True
        for j in yeni_hece:
        #dosya = "/home/boncul/Masaüstü/Kodlar/sesler/" + j + ".mp3"

        #print u'/home/boncul/Kodlar/sesler/' + j + u'.mp3'

            if (os.path.exists(u'/home/boncul/Masaüstü/m2ses/' + j + u'.mp3') == True):
                #denge = True
                continue
            else:
                denge = False

        if (denge == True):
            #hece_son = unicode(hece_son, 'utf8')
            cal(yeni_hece)
        else:
            #harf_son = unicode(harf_son, 'utf8')
            cal(harfle(word))


def cal(m=list()):
    #m=islem_yapan(veri)

    for i in m:
        s = i + ".mp3"

        import pygst
        
        pygst.require("0.10")

        import gst
        
        player = gst.Pipeline("player")
        source = gst.element_factory_make("filesrc", "file-source")
        decoder = gst.element_factory_make("mad", "decoder") #mp3 formatı için decoder "mad", örneğin flac için "flacdec"...

        conv = gst.element_factory_make("audioconvert", "converter")
        sink = gst.element_factory_make("autoaudiosink", "audio-output") #autoaudiosink yerine sistemin kullandığı ses aygıtı, örneğin "alsasink", "alsa-output" yazılabilir

        player.add(source, decoder, conv, sink)

        gst.element_link_many(source, decoder, conv, sink)

        player.get_by_name("file-source").set_property("location", s) #aynı dizinde değilse tam yol yazılmalı
        player.set_state(gst.STATE_PLAYING)

        time.sleep(0.40)
        player.set_state(gst.STATE_NULL)
        #raw_input()
def cal2(m=list()):
    #m=islem_yapan(veri)

    for i in m:
        s = i + ".mp3"

        import pygst
        
        pygst.require("0.10")

        import gst
        
        player = gst.Pipeline("player")
        source = gst.element_factory_make("filesrc", "file-source")
        decoder = gst.element_factory_make("mad", "decoder") #mp3 formatı için decoder "mad", örneğin flac için "flacdec"...

        conv = gst.element_factory_make("audioconvert", "converter")
        sink = gst.element_factory_make("autoaudiosink", "audio-output") #autoaudiosink yerine sistemin kullandığı ses aygıtı, örneğin "alsasink", "alsa-output" yazılabilir

        player.add(source, decoder, conv, sink)

        gst.element_link_many(source, decoder, conv, sink)

        player.get_by_name("file-source").set_property("location", s) #aynı dizinde değilse tam yol yazılmalı
        player.set_state(gst.STATE_PLAYING)

        time.sleep(0.35)
        player.set_state(gst.STATE_NULL)
        #raw_input()

pencere = Tkinter.Tk()
pencere.title("M2SES v1.0")

pgen = 600
pyuks = 350
ekrangen = pencere.winfo_screenwidth()
ekranyuks = pencere.winfo_screenheight()
x = (ekrangen - pgen) / 2
y = (ekranyuks - pyuks) / 2
pencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))

pencere.tk_setPalette("#DDDBD1")
etiket = Label(text="SESLENDİRİLECEK CÜMLEYİ GİRİNİZ",font="Helvetica 12 bold")
etiket.pack()
giris = Text(bd=7,bg="#ffffff",width=75,height=13)
giris.pack()

def dosya_al():
    file = tkFileDialog.askopenfile(parent=pencere,mode='rb',title='Choose a file')
    if file != None:
        global veri
        veri = file.read()
        file.close()
        islem_yapan(veri)
        # print "I got %d bytes from this file." % len(data)

def girdi_al():
    global veri
    veri = giris.get('1.0','end')
    veri = unicode.encode(unicode(veri),"utf8")
    islem_yapan(veri)
    
giris.delete(1.0,2.0)
cerceve = Frame()
cerceve.pack()
dugme = Button(text="Dosyadan Oku",bg = "#BFBAAF", command=dosya_al)
dugme.pack(padx=35,pady=25,side=LEFT)

dugme = Button(text="Çıkış",bg = "#8b0000",fg="white",command=pencere.quit )
dugme.pack(padx=55,pady=25,side=RIGHT)

dugme = Button(text="Seslendir",bg = "#BFBAAF",command=girdi_al)
dugme.pack(padx=75,pady=25,side=RIGHT)
pencere.mainloop()
