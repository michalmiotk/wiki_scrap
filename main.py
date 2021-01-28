import wikipediaapi
from bs4 import BeautifulSoup
import re

from extract_links import get_links

wiki_html = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
        )

for wiki_page_name in get_links():
    #if wiki_page_name.startswith("wiki")
    if wiki_page_name.startswith("/wiki/"):
        page_name = wiki_page_name.lstrip("/wiki/")
        print(page_name)
        ngousa = wiki_html.page(page_name)
        print(ngousa.summary)
    else:
        print("not wiki link", wiki_page_name)

'''
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