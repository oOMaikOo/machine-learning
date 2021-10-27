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
import subprocess
import os
import difflib
import time

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
				subprocess.call(['wget', "https://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip"])
				print("##### Download finish #####\n\n\n")
				download = True
				file.close()
				file = open("date.txt","w")
				file.write(str(line)[28:50])
				file.close()
				subprocess.call(['unzip' , 'FLAT_RCL.zip'])
			else:
				print("##### No new recalls at NHTSA online #####")
				download = False
#data.close()

if download == True:
	new_count = 0
	old_count = 0
	count = 0
	subprocess.call(['rm', 'FLAT_RCL.zip'])
	subprocess.call(['mv', 'RECL_NEW.txt', 'RECL_OLD.txt'])
	subprocess.call(['mv', 'FLAT_RCL.txt', 'RECL_NEW.txt'])
	time.sleep(10)

	with open('RECL_NEW.txt', 'r') as new_file,open('RECL_OLD.txt', 'r') as old_file:
		for l1 in new_file:
			new_count += 1
		for l2 in old_file:
			old_count += 1
	new_file.close()
	old_file.close()

	with open('RECL_NEW.txt', 'r') as new_file,open('RECL_OLD.txt', 'r') as old_file:
		for l1 in new_file:
			if count <= old_count:
				count += 1
			else:
				print("##### We have new recalls #####\n\n\n"+l1)
	new_file.close()
	old_file.close()
