from Parser.parse_main import load_file
from nlp.nlp_main import lines_to_sentences, word2vec
from gensim.models import Word2Vec
from crawler.crawl_main import get_synonym
import os


class W2VModel:
    def __init__(self, contents, model_path):
        sentences = lines_to_sentences(contents)
        if os.path.exists(model_path):
            self.model = Word2Vec.load(model_path)
        else:
            self.model = word2vec(sentences)
            self.model.save(model_path)
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
    model = W2VModel(contents, f'model/{model_name}.embedding')

    return model


if __name__ == '__main__':
    from nltk.corpus import wordnet

    w2v_model = create_model()
    w2v = w2v_model.model
    vocabs = list(w2v.wv.vocab.keys())

    sentence = 'there was a great deal more that was delightful'
    sentence = sentence.lower()

    adj = []

    for word in sentence.split():
        for synset in wordnet.synsets(word):
            if word in str(synset) and '.a.' in str(synset):
                if word not in adj:
                    adj.append(word)

    print(adj)

    for word in adj:
        synonyms = []

        if word in vocabs:
            similar = w2v.wv.most_similar(word)
            synonyms.extend(get_synonym(word))
            for i in range(min(5, len(similar))):
                synonyms.extend(get_synonym(similar[i][0]))

        for syn in synonyms:
            print(sentence.replace(word, syn))
