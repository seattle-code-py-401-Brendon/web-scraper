import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/American_Civil_War'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
prettier_soup = soup.findAll(text='citation needed')

for text in prettier_soup:
    soup_text = text.findParent('p')
    soup_text = soup_text.text.split()
    string_text = ' '.join(soup_text)
    print(string_text)
    print('-------------------------------------------------------------------------')

citations_count = len(prettier_soup)
print(f'{citations_count} citations needed')
