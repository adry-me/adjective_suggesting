from urllib.request import urlopen
from bs4 import BeautifulSoup


def crawl_yourdictionary():
    response = urlopen('https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html')
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    return [td.text.lower() for td in soup.find('table').find_all('td') if td.find('strong') is None]

    #table = soup.find('table')
    #tbody = table.find('tbody')
    #tr = tbody.find_all('tr')
    #for tr_elem in tr:
    #    td = tr_elem.find_all('td')
    #    for td_elem in td:
    #        if td_elem.find('strong') is None:
    #            print(td_elem.text.lower())


if __name__ == '__main__':
    crawl_yourdictionary()