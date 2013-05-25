#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

def cal(veri):
    m=islem_yapan(veri)
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
        time.sleep(0.30)
        player.set_state(gst.STATE_NULL)
        #raw_input()
