#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xml.etree import ElementTree as ET
ET.register_namespace('com',"http://www.company.com") #some name

# build a tree structure
root = ET.Element("{http://www.company.com}STUFF")
body = ET.SubElement(root, "{http://www.company.com}MORE_STUFF")
body.text = "STUFF EVERYWHERE!"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

tree.write("page1.xml",
           xml_declaration=True,encoding='utf-8',
           method="xml")
#  write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None, method="xml", *, short_empty_elements=True)¶
#########
from xml.etree import ElementTree as ET

# build a tree structure
root = ET.Element("{http://www.company.com}STUFF")
body = ET.SubElement(root, "{http://www.company.com}MORE_STUFF")

body.text = "STUFF EVERYWHERE!"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

tree.write("page2.xml",
           xml_declaration=True, encoding='utf-8',
           method="xml", default_namespace='http://www.company.com')
##
from xml.etree import ElementTree as ET
root = ET.Element("STUFF")
root.set('com','http://www.company.com')
body = ET.SubElement(root, "MORE_STUFF")
body.text = "STUFF EVERYWHERE!"

tree.write("page3.xml",
           xml_declaration=True, encoding='utf-8',
           method="xml", default_namespace='http://www.company.com')

###########
namespaces = {'owl': 'http://www.w3.org/2002/07/owl#'} # add more as needed

root.findall('owl:Class', namespaces=namespaces)
from xml.etree import ElementTree as ET

tree = ET.parse("page1.xml")
doc = tree.getroot()
thingy = doc.find('timeSeries')
if thingy is not None:
    print(thingy.attrib)

##
for elem in doc.findall('timeSeries/values/value'):
    print(elem.get('dateTime'), elem.text)
    ##########
values = doc.find('timeSeries/values')
for value in values:
    print(value.get('dateTime'), elem.text)
