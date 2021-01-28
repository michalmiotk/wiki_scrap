from bs4 import BeautifulSoup

from extract_links import extract_links

soup = BeautifulSoup(extract_links(), 'html')

for link in soup.find_all('a'):
    print(link.get('href'))