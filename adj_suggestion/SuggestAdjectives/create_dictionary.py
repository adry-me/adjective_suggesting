from urllib.request import urlopen
from bs4 import BeautifulSoup
from .models import Adjective
import os
import sys
sys.path.append(os.path.dirname(
    os.path.abspath(
        os.path.dirname(
            os.path.abspath(
                os.path.dirname(
                    __file__
                )
            )
        )
    )
))
from crawler.crawl_tuna import get_synonyms
from main import find_syn_adj, create_model


def save(words):
    saved_objects = []
    for word in words:
        objects = Adjective.objects.filter(word=word)
        if len(objects) > 0:
            saved_objects.append(objects[0])
            continue
        adj = Adjective(word=word)
        adj.save()
        saved_objects.append(adj)

    return saved_objects


def create_synonyms(words):
    # w2v_model = create_model()
    for word in words:
        adj_objects = Adjective.objects.filter(word=word)
        if len(adj_objects) == 0:
            adj = Adjective(word=word)
        else:
            if len(adj_objects) != 1:
                print(f'*** WARNING *** length of {word} = {len(adj_objects)}')
            adj = adj_objects[0]

        # syn_gen = find_syn_adj('', word, w2v_model)
        synonyms = get_synonyms(word)

        if len(synonyms) > 0:
            if len(adj_objects) == 0:
                adj.save()
        synonym_objects = save(synonyms)
        for syn_obj in synonym_objects:
            adj.synonyms.add(syn_obj)



def crawl_yourdictionary():
    response = urlopen('https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html')
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    return [td.text.lower() for td in soup.find('table').find_all('td') if td.find('strong') is None]


def load_adjectives(path):
    if os.path.exists(path):
        with open(path) as f:
            adjectives = list(map(str.rstrip, f.readlines()))
    else:
        adjectives = crawl_yourdictionary()

    return adjectives


def filter_exclude(words):
    result = []
    index = 0
    while index < len(words):
        objects = Adjective.objects.exclude(
            word__in=words[index:min(len(words), index+900)]
        )
        index += 900

        result.extend([obj.word for obj in objects])

    return result


# from SuggestAdjectives.create_dictionary import *
def main(loop=5):
    os.chdir('..')
    path = 'model/saved_adjectives.txt'
    adjectives = load_adjectives(path)
    completed = []

    for i in range(loop):
        save(adjectives)
        create_synonyms(adjectives)

        completed.extend(adjectives)
        with open(path, 'w', encoding='utf-8') as f:
            for word in completed:
                f.write(f'{word}\n')
        print(f'loop {i + 1} completed')

        adjectives = filter_exclude(completed)

    exit()

