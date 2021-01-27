import wikipediaapi
from bs4 import BeautifulSoup
import re

wiki_html = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
        )
ngousa = wiki_html.page("List_of_environmental_and_conservation_organizations_in_the_United_States")
print(ngousa.links)
links = []
def print_sections(sections, level=0):
    for s in sections:
        #print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
        if s.title not in ['Government agencies', 'See also']:
            soup = BeautifulSoup(s.text, 'html.parser')
            print(s.title, " no i gdzie tekst ? ? ? ? ?")
            print(s.full_text())
            
            print("SOUP******************")
            #soup.prettify()
        print_sections(s.sections, level + 1)
print_sections(ngousa.sections)
'''
for i,link in enumerate(links):
    if key == "Environmental community organizations":
        print("xxxx")
    print(value)
    if i == 2222:
        wiki_html = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
        )
        p_html = wiki_html.page(key)
        #print(p_html.text)
        print("SUMARY")
        (p_html.summary)
        print("SUMARY")
        def print_sections(sections, level=0):
            
            for s in sections:
                    #print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
                    soup = BeautifulSoup(s.text, 'lxml')
                    print("SOUP******************")
                    print(s.title)
                    print(soup.text)
                    print("SOUP******************")
                    print_sections(s.sections, level + 1)
        print_sections(p_html.sections)
'''