from Parser.parse_main import load_file
from nlp.nlp_main import lines_to_sentences, word2vec, analyze_text
from gensim.models import Word2Vec
from crawler.crawl_main import get_synonyms, get_antonyms
from nltk.corpus import wordnet
import os

from nlp.synonymgenerator import SynonymGenerator


class W2VModel:
    def __init__(self, contents, model_path):
        sentences = lines_to_sentences(contents)
        if os.path.exists(model_path):
            self.model = Word2Vec.load(model_path)
        else:
            self.model = word2vec(sentences)
            self.model.save(model_path)
        self.contents = contents
        self.vocabs = list(self.model.wv.vocab.keys())

    def get_combined_text(self):
        return '\n'.join(self.contents)

    def get_vocabs(self):
        return self.vocabs

    def most_similar(self, word):
        return self.model.wv.most_similar(word)

    def similarity(self, word1, word2):
        return self.model.wv.similarity(word1, word2)


def collect_all(suffix='_mod'):
    fnames = [filename for filename in os.listdir('data') if suffix in filename]

    contents = []
    for filename in fnames:
        contents.extend(load_file(f'data/{filename}'))

    return contents


def create_model(model_name='v1', suffix='_mod'):
    contents = collect_all(suffix)
    model = W2VModel(contents, f'model/{model_name}.embedding')

    return model


def parse_input(sentence):
    sentence = sentence.lower()

    adj = []

    for word in sentence.split():
        for synset in wordnet.synsets(word):
            if word in str(synset) and '.a.' in str(synset):
                if word not in adj:
                    adj.append(word)
    return adj


def find_syn_adj(line, adj, w2v_model):
    syn_gen = SynonymGenerator(line, adj)
    syn_gen.create(w2v_model)

    return syn_gen


def find_syn_line(line, w2v_model):
    w2v = w2v_model.model
    vocabs = w2v_model.get_vocabs()

    line_result = [line]
    for word in parse_input(line):
        syn_gen = find_syn_adj(line, word, w2v_model)
        line_result.extend(syn_gen.generate())

    return line_result


def find_syn(text, w2v_model):
    w2v = w2v_model.model
    vocabs = w2v_model.get_vocabs()

    result = []

    for line in text:
        result.append(find_syn_line(line, w2v_model))

    return result


def main(target_path):
    with open(target_path) as f:
        lines = list(map(str.strip, f.readlines()))

    w2v_model = create_model()
    find_syn(lines, w2v_model)

if __name__ == '__main__':
    print(parse_input('He is defiant'))