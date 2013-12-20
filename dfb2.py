#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import traceback
import base64

def heavy_dom(xmlinfile, encoding="UTF-8"):
    from xml.dom.minidom import parse, parseString
    try:
        with parse(xmlinfile) as dom:
            p_list = dom.getElementsByTagName("binary")
            for p in p_list:
                if not p.hasChildNodes():
                    continue
                name = p.getAttribute("id")
                for node in p.childNodes:
                    if node.nodeType == node.TEXT_NODE:
                        s = node.data
                        data = base64.b64decode(s)
                        
                        with open(name, "wb") as f:
                            f.write(data)
            #with open(xmloutfile, "w", encoding=encoding) as f:
            #    dom.writexml(f, indent="\n", addindent=" ",encoding=encoding)
    except Exception as e:
        print(e)
        traceback.print_exc()

def add_images_dom(xmlinfile, xmloutfile, encoding="UTF-8"):
    from xml.dom.minidom import parse, parseString
    import os
    try:
        with parse(xmlinfile) as dom:
            fb = dom.getElementsByTagName("FictionBook")[0]
            for i in range(26):
                image_filename = "_%s.jpg" %i
                print(image_filename)
                with open(image_filename, "rb") as f_im:
                    data = f_im.read()
                    data = base64.b64encode(data)
                    binary_el = dom.createElement("binary")
                    imname = os.path.basename(image_filename)
                    im, tp = imname.split(".")
                    binary_el.setAttribute("id", imname)
                    if tp in ["jpg", "jpeg"]:
                        tp = "jpeg"
                    elif tp == ".png":
                        tp="png"
                    binary_el.setAttribute("content-type","image/"+tp)
                    im_el = dom.createTextNode(data.decode(encoding)) #or may use str(data, 'utf-8')
                    binary_el.appendChild(im_el)
                    fb.appendChild(binary_el)
            with open(xmloutfile, "w", encoding=encoding) as f:
                dom.writexml(f, 
                    #indent="\n", addindent=" ",
                    #encoding=encoding
                    )
    except Exception as e:
        print(e)
        traceback.print_exc()

import xml.dom.minidom as dom
impl = dom.getDOMImplementation()
newdoc = impl.createDocument("http://www.gribuser.ru/xml/fictionbook/2.0", "FictionBook", None)
top_element = newdoc.documentElement
top_element.setAttribute("xmlns", "http://www.gribuser.ru/xml/fictionbook/2.0")
top_element.setAttribute("xmlns:xlink", \
                            "http://www.w3.org/1999/xlink")
    
description_element = newdoc.createElement("description")
top_element.appendChild(description_element)
with codecs.open(foutname, "w", encoding="utf-8") as f:
    newdoc.writexml(f, indent="\n", addindent=" ",encoding="utf-8")
