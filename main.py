from parse_main import load_file
from nlp.nlp_main import lines_to_sentences, word2vec

if __name__ == '__main__':
    contents = []
    contents.extend(load_file('data/P_P_mod.txt'))
    contents.extend(load_file('data/S_S_mod.txt'))
    contents.extend(load_file('data/M_P_mod.txt'))

    from nltk.corpus import movie_reviews
    mv_sentences = [list(s) for s in movie_reviews.sents()]

    sentences = lines_to_sentences(contents)
    print(len(sentences))
    model = word2vec(mv_sentences)
    vocabs = list(model.wv.vocab.keys())

    print(len(vocabs))
    print(vocabs)
    print(model.most_similar('he'))

    import random
    for _ in range(10):
        word1 = vocabs[random.randint(0, len(vocabs) - 1)]
        word2 = vocabs[random.randint(0, len(vocabs) - 1)]
        sim  = model.wv.similarity(word1, word2)
        print(word1, word2, sim)