import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import xml.etree.ElementTree as ET
url = 'https://en.wikipedia.org/wiki/List_of_environmental_and_conservation_organizations_in_the_United_States'
html = urlopen(url)
soup = BeautifulSoup(html, 'xml')
good_val = ''
turn_grab=False
soup_split = str(soup).split("\n")
joining_on = False
for s in soup_split:
    if s.find("Alphabetical listing") > -1:
        joining_on = True
    
    if s.find("References") > -1:
        joining_on = False
        print("found refere")
    if joining_on:
        good_val.join(' ').join(s)

