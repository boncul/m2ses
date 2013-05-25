#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

sesli  = [u'a', u'e', u'ı', u'i', u'o', u'ö', u'u', u'ü', u'A', u'E', u'I', u'i', u'O', u'Ö', u'U', u'Ü']
sessiz = [u'b', u'c', u'ç', u'd', u'f', u'g', u'ğ', u'h', u'j', u'k', u'l', u'm', u'n', u'p', u'r', u's',
          u'ş', u't', u'v', u'y', u'z', u'B', u'C', u'Ç', u'D', u'F', u'G', u'Ğ', u'H', u'J', u'K', u'L',
          u'M', u'N', u'P', u'R', u'S', u'Ş', u'T', u'V', u'Y', u'Z' ]

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

def hece(kelime):
    if len(kelime)==1 or len(kelime)==2 and kelime[1] in sessiz and kelime[0] in sesli:
        return ('', kelime)
    if len(kelime)==3 and kelime[0] in sesli:
        return ('', kelime)

    kelime = kelime[::-1]

    for i in kelime:
        if i in sesli:
            break

    n = kelime.find(i)
    if kelime[n+1] in sessiz:
        return ( kelime[n+2:][::-1] , kelime[:n+2][::-1] )
    if kelime[n+1] in sessiz:
        return ( kelime[n+2:][::-1] , kelime[:n+2][::-1] )
    else:
        return ( kelime[n+1:][::-1] , kelime[:n+1][::-1] )

def hecele(kelime):
    kelime=kucukHarfCevir(kelime)
    kelime = unicode(kelime , 'utf8')
    kelime = ''.join([ i for i in kelime if i in sesli or i in sessiz])
    heceler = list()
    while True:
        if kelime=='':
            break
        ( kelime , ek ) = hece(kelime)
        heceler.append(ek)
    heceler=heceler[::-1]
    #y_heceler = list()
    #for j in range(len(heceler)):
    #    y_heceler.append(heceler[j].encode('utf-8', 'ignore'))
    return heceler

def harfle(kelime):
    kelime = kucukHarfCevir(kelime)
    kelime = unicode(kelime , 'utf8')
    harfler = list()

    for i in range(len(kelime)):
        harfler.append(kelime[i])

    return harfler

def islem_yapan(cumle):
    cumle = kucukHarfCevir(cumle)
    #cumle = unicode(cumle, 'utf8')
    cumle = cumle.strip('."\',;')
    kelimeler = cumle.split()
    hece_son = list()
    harf_son = list()

    for k in kelimeler:
        harf_son = harf_son + harfle(k)
        #harf_son.append(harfle(k))
        
    for i in kelimeler:
        hece_son = hece_son + hecele(i)
        #hece_son.append(hecele(i))
        
    denge = True
    kontrol = list()
    for j in hece_son:
        #dosya = "/home/boncul/Masaüstü/Kodlar/sesler/" + j + ".mp3"
        
        #print u'/home/boncul/Kodlar/sesler/' + j + u'.mp3'
        if (os.path.exists(u'/home/boncul/Kodlar/sesler/' + j + u'.mp3') == True):
            #denge = True
            continue
        else:
            denge = False
            
        
    if (denge == True):
        #hece_son = unicode(hece_son, 'utf8')
        return hece_son
    else:
        #harf_son = unicode(harf_son, 'utf8')
        return harf_son

    
    
