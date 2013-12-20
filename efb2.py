#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xml.etree import ElementTree as ET
ET.register_namespace('',"http://www.gribuser.ru/xml/fictionbook/2.0") #some name

# build a tree structure
root = ET.Element("{http://www.gribuser.ru/xml/fictionbook/2.0}FictionBook")
root.set('xmlns:xlink',"http://www.w3.org/1999/xlink")
body = ET.SubElement(root, "{http://www.gribuser.ru/xml/fictionbook/2.0}description")
body.text = "STUFF EVERYWHERE!"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

tree.write("page1.xml",
           xml_declaration=True, encoding='utf-8',
           method="xml")
#  write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None, method="xml", *, short_empty_elements=True)¶
#########
from xml.etree import ElementTree as ET

# build a tree structure
root = ET.Element("{http://www.gribuser.ru/xml/fictionbook/2.0}FictionBook")
root.set('xmlns:xlink', "http://www.w3.org/1999/xlink")
body = ET.SubElement(root, "{http://www.gribuser.ru/xml/fictionbook/2.0}description")

body.text = "STUFF EVERYWHERE!"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

tree.write("page2.xml",
          xml_declaration=True, encoding='utf-8',
          method="xml")
#######
from xml.etree import ElementTree as ET
root = ET.Element("FictionBook")
root.set('',"http://www.gribuser.ru/xml/fictionbook/2.0")
root.set('xlink',"http://www.w3.org/1999/xlink")
body = ET.SubElement(root, "description")
body.text = "STUFF EVERYWHERE!"

tree.write("page3.xml",
           xml_declaration=True, encoding='utf-8',
           method="xml")
