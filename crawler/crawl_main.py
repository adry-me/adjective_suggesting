from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def valid_entry_check(entry):
    """
            Check if input is null or contains only spaces or numbers or special characters
            """
    temp = re.sub(r'[^A-Za-z ]', ' ', self.entry)
    temp = re.sub(r"\s+", " ", temp)
    temp = temp.strip()
    if temp != "":
        return True
    return False


def get_synonym(entry):
    result = []
    if True:
        response = urlopen(f'http://www.thesaurus.com/browse/{entry}')
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')

        # main div for synonym (comes first) and antonym
        main_ul = soup.find('ul', {'class': 'css-1ytlws2 et6tpn80'})
        # span tag for each word
        for main_span in main_ul.findAll('span', {'class': 'css-133coio etbu2a32'}):
            for a_tag in main_span.findAll('a'):
                result.append(a_tag.text)
    else:
        print(f'ERROR: invalid input - {entry}')

    return result
