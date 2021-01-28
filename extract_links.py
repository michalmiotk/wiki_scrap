import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import xml.etree.ElementTree as ET
def extract_text():
    url = 'https://en.wikipedia.org/wiki/List_of_environmental_and_conservation_organizations_in_the_United_States'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'xml')
    good_val = ''
    turn_grab=False
    soup_split = str(soup).split("\n")
    joining_on = False
    for s in soup_split:
        if s.find("References") > -1:
            joining_on = False
        if joining_on:
            good_val += s
        if s.find("Alphabetical listing") > -1:
            joining_on = True
        
        
        

    return good_val

def get_links():
    soup = BeautifulSoup(extract_text(), 'html')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links
