import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    prettier_soup = soup.findAll(text='citation needed')
    citations_count = len(prettier_soup)
    print(f'{citations_count} citations needed')


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    prettier_soup = soup.findAll(text='citation needed')
    single_parent = prettier_soup[0]
    soup_parents = single_parent.findParent('p')
    soup_text = soup_parents.text.split()
    string_text = ' '.join(soup_text)
    print(string_text)


if __name__ == '__main__':
    corgi_url = 'https://en.wikipedia.org/wiki/Welsh_Corgi'
    get_citations_needed_count(corgi_url)
    get_citations_needed_report(corgi_url)
