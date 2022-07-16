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

    for text in prettier_soup:
        soup_text = text.findParent('p')
        soup_text = soup_text.text.split()
        string_text = ' '.join(soup_text)
        print(string_text)
        print('-------------------------------------------------------------------------')


if __name__ == '__main__':
    civil_war_url = 'https://en.wikipedia.org/wiki/American_Civil_War'
    get_citations_needed_count(civil_war_url)
    get_citations_needed_report(civil_war_url)
