from parse_main import load_file
from nlp.nlp_main import lines_to_sentences, word2vec, analyze_text
from crawler.crawl_main import get_synonym
import os


class W2VModel:
    def __init__(self, contents):
        sentences = lines_to_sentences(contents)
        self.model = word2vec(sentences)
        self.contents = contents

    def get_combined_text(self):
        return '\n'.join(self.contents)


def collect_all(suffix='_mod'):
    fnames = [filename for filename in os.listdir('data') if suffix in filename]

    contents = []
    for filename in fnames:
        contents.extend(load_file(f'data/{filename}'))

    return contents


def create_model(suffix='_mod'):
    contents = collect_all(suffix)
    sentences = lines_to_sentences(contents)
    model = W2VModel(contents)

    return model


if __name__ == '__main__':
    w2v_model = create_model()
    w2v = w2v_model.model
    vocabs = list(w2v.wv.vocab.keys())

    import random

    for _ in range(10):
        word1 = vocabs[random.randint(0, len(vocabs) - 1)]
        word2 = vocabs[random.randint(0, len(vocabs) - 1)]
        sim = w2v.wv.similarity(word1, word2)
        print(word1, word2, sim)

    word = 'happy'
    syn_list = []

    syn_list.extend(get_synonym(word)[:5])
    for i in range(3):
        syn_list.extend(get_synonym(w2v.wv.most_similar(word)[i][0])[:5])

    adj_list, count = analyze_text(w2v_model.get_combined_text())

    for syn in syn_list:
        if syn in adj_list:
            print(syn, count[syn])