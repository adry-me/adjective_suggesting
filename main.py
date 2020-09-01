from parse_main import load_file
from nlp.nlp_main import lines_to_sentences, word2vec

if __name__ == '__main__':
    contents = load_file('P_P_mod.txt')

    from nltk.corpus import movie_reviews
    mv_sentences = [list(s) for s in movie_reviews.sents()]

    sentences = lines_to_sentences(contents)
    print(len(sentences))
    model = word2vec(sentences)
    vocabs = model.wv.vocab

    print(model.most_similar('he'))

    import random
    for _ in range(10):
        s1 = sentences[random.randint(0, len(sentences) - 1)]
        s2 = sentences[random.randint(0, len(sentences) - 1)]
        word1 = s1[random.randint(0, len(s1) - 1)]
        word2 = s2[random.randint(0, len(s2) - 1)]
        sim  = model.wv.similarity(word1, word2)
        print(word1, word2, sim)