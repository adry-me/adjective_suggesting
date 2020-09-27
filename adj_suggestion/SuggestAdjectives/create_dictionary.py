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
from crawler.crawl_main import get_synonyms


def save(words):
    saved_objects = []
    for word in words:
        objects = Adjective.objects.filter(word=word)
        if len(objects) > 0:
            saved_objects.append(objects[0])
        adj = Adjective(word=word)
        adj.save()
        saved_objects.append(adj)

    return saved_objects


def create_synonyms(words, line):
    for word in words:
        adj_objects = Adjective.objects.filter(word=word)
        if len(adj_objects) != 1:
            print(f'*** WARNING *** length of {word} = {len(adj_objects)}')
        adj = adj_objects[0]

        syn_w2v_list = []
        w2v_model = main.create_model()
        syn_w2v = main.find_syn_adj(line, adj, w2v_model)
        syn_w2v_list.append(syn_w2v)
        synonyms = Adjective(word=adj)
        synonyms.save()
        syn_w2v_objects = save(syn_w2v.synonyms)
        for syn_w2v in syn_w2v_objects:
            synonyms.synonyms.add(syn_w2v)
        synonym_objects = save(synonyms)
        for syn_obj in synonym_objects:
            adj.synonyms.add(syn_obj)



def crawl_yourdictionary():
    response = urlopen('https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html')
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    return [td.text.lower() for td in soup.find('table').find_all('td') if td.find('strong') is None]

#if __name__ == '__main__':
#    adj_objects = Adjective.object.all()
#    create_synonyms([adj.word for adj in adj_objects])

# from SuggestAdjectives.create_dictionary import *
# save(crawl_yourdictionary())


def main():
    basic_adjectives = crawl_yourdictionary()
    save(basic_adjectives)
#    create_synonyms(basic_adjectives, input)
    exit()
