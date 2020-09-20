from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


_max_caches = 5
_cache = []


class _Cache:
    def __init__(self, word, contents):
        self.word = word
        self.contents = contents
        self.hit = 0

    def get(self):
        self.hit += 1
        return self.contents


def _get_html(word):
    word_list = [cache.word for cache in _cache]
    if word in word_list:
        idx = word_list.index(word)
        return _cache[idx].get()

    try:
        response = urlopen(f'http://www.thesaurus.com/browse/{word}')
    except HTTPError:
        return None
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    new_cache = _Cache(word, soup)

    if len(_cache) == _max_caches:
        hit_list = [cache.hit for cache in _cache]
        idx = hit_list.index(min(hit_list))
        _cache.pop(idx)

    _cache.append(new_cache)

    return new_cache.get()


def _parse_thesaurus_div(div):
    ul = div.find('ul')
    li_list = ul.find_all('li')
    words = {}
    css_keys = []

    for li in li_list:
        a_tag = li.find('a')
        class_name = ' '.join(a_tag.attrs.get('class', ['EMPTY_CLASS']))
        if class_name not in css_keys:
            css_keys.append(class_name)
            words[class_name] = []

        words[class_name].append(a_tag.text)

    return words[css_keys[0]]


def _parse_soup(soup):
    main_section = soup.find('section', {'class': 'MainContentContainer'}).find('section', recursive=False)
    # div 0: word
    # div 1: syn
    # div 2: swap
    # div 3: ant
    div_list = main_section.find_all('div', recursive=False)
    syn_div = div_list[1]
    ant_div = div_list[3]

    return _parse_thesaurus_div(syn_div), _parse_thesaurus_div(ant_div)


def valid_entry_check(entry):
    """
            Check if input is null or contains only spaces or numbers or special characters
            """
    temp = re.sub(r'[^A-Za-z ]', ' ', entry)
    temp = re.sub(r"\s+", " ", temp)
    temp = temp.strip()
    if temp != "":
        return True
    return False


def get_synonyms(entry):
    soup = _get_html(entry)
    if soup is None:
        return []

    syn, _ = _parse_soup(soup)

    return syn


def get_antonyms(entry):
    soup = _get_html(entry)
    if soup is None:
        return []

    _, ant = _parse_soup(soup)

    return ant

if __name__ == '__main__':
    _parse_soup(_get_html('good'))