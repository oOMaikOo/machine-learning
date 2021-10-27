# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:54:54 2018

@author: maikloehn
Update
"""

#!/bin/env/ python

# Webiste https://www-odi.nhtsa.dot.gov/downloads/index.cfm
# Website parser
# Source adress for Recal inforamation USA
# https://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip
# https://www.adac.de/infotestrat/reparatur-pflege-und-wartung/rueckrufe/
# https://www.kfz-rueckrufe.de/
# New Update
from bs4 import BeautifulSoup

import sys
import requests
import wget
import subprocess
import os
import difflib
import time
import zipfile

url = 'https://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip'
path_to_zip_file = 'FLAT_RCL.zip'
directory_to_extract_to = ''
#urllib.request.urlretrieve(url, 'FLAT_RCL.zip') 

os.system("clear")
print ("Loading...")

if os.path.exists("RECL_OLD.txt"):
	subprocess.call(['rm', 'RECL_OLD.txt'])

file = open("date.txt","r")

data = file.read()
html = requests.get("https://www-odi.nhtsa.dot.gov/downloads/index.cfm").text
soup = BeautifulSoup(html, 'html5lib')

count = 0
download = None

first_paragraph = soup('div', 'downloadcenter')

for line in first_paragraph:
    if '><' in str(line):
        pass
    else:
        count += 1
        if count == 6:
            if (str(line)[28:50]) != data:
                wget.download(url)
                print("##### Download finish #####\n\n\n")
                download = True
                file.close()
                file = open("date.txt","w")
                file.write(str(line)[28:50])
                file.close()
                zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
                zip_ref.extractall(directory_to_extract_to)
                zip_ref.close()
            else:
                print("##### No new recalls at NHTSA online #####")
                download = False

