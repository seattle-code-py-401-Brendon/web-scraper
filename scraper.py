import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Welsh_Corgi'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
prettier_soup = soup.findAll(text='citation needed')
single_parent = prettier_soup[0]
soup_parents = single_parent.findParent('p')

# for item in soup_parents:
#     print(item)

soup_text = soup_parents.text.split()

string_text = ' '.join(soup_text)
print(string_text)
citations_count = len(prettier_soup)
print(f'{citations_count} citations needed')
