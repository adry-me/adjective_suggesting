from Parser.parse_main import load_file
from nlp.nlp_main import lines_to_sentences, word2vec, analyze_text
from gensim.models import Word2Vec
from crawler.crawl_main import get_synonyms, get_antonyms
from nltk.corpus import wordnet
import os


class W2VModel:
    def __init__(self, contents, model_path):
        sentences = lines_to_sentences(contents)
        if os.path.exists(model_path):
            self.model = Word2Vec.load(model_path)
        else:
            self.model = word2vec(sentences)
            self.model.save(model_path)
        self.contents = contents

    def get_combined_text(self):
        return '\n'.join(self.contents)


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


def create_vocabs(w2v_model):
    w2v = w2v_model.model
    vocabs = list(w2v.wv.vocab.keys())

    return vocabs


def parse_input(sentence):
    sentence = sentence.lower()

    adj = []

    for word in sentence.split():
        for synset in wordnet.synsets(word):
            if word in str(synset) and '.a.' in str(synset):
                if word not in adj:
                    adj.append(word)
    return adj


def find_syn(text, w2v_model):
    w2v = w2v_model.model
    vocabs = create_vocabs(w2v_model)

    result = []

    for line in text:
        line_result = []
        line_result.append(line)
        for word in parse_input(line):
            synonyms = {}
            if word in vocabs:
                similar = w2v.wv.most_similar(word)
                synonyms[word] = get_synonyms(word)
                antonyms = get_antonyms(word)

                idx = 0
                count = 0
                while idx < len(similar):
                    sim = similar[idx][0]

                    dist = 0
                    dist_cnt = 0
                    for ant in antonyms:
                        if ant in vocabs:
                            dist += w2v.wv.similarity(ant, sim)
                            dist_cnt += 1

                    if dist_cnt != 0:
                        dist = dist / dist_cnt

                    if sim not in antonyms and (dist_cnt == 0 or dist < 0.2):
                        synonyms[sim] = get_synonyms(sim)
                        count += 1

                    if count == 5:
                        break

                    idx += 1

            print(f'============={word}=============')
            for syn_key in synonyms:
                print(f'-- {syn_key} --')
                for syn in synonyms[syn_key]:
                    newline = line.replace(word, syn)
                    print(newline)
                    if syn[0] in {"a", "e", "i", "o", "u"}:
                        wordsinline = newline.split()
                        word_before_adj = wordsinline[wordsinline.index(syn) - 1]
                        if word_before_adj == "a":
                            line_result.append(newline.replace(" a ", " an "))
                        else:
                            line_result.append(newline)
                    elif syn[0] not in {"a", "e", "i", "o", "u"}:
                        wordsinline = newline.split()
                        word_before_adj = wordsinline[wordsinline.index(syn) - 1]
                        if word_before_adj == "an":
                            line_result.append(newline.replace(" an ", " a "))
                        else:
                            line_result.append(newline)

                    else:
                        line_result.append(newline)
        result.append(line_result)

    return result


def main(target_path):
    with open(target_path) as f:
        lines = list(map(str.strip, f.readlines()))

    w2v_model = create_model()
    find_syn(lines, w2v_model)

if __name__ == '__main__':
    main('data/test_sample.txt')