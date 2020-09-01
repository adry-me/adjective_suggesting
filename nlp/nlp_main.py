from gensim.models.word2vec import Word2Vec


def lines_to_sentences(lines):
    return list(map(str.split, lines))


def word2vec(lines):
    model = Word2Vec(lines)
    model.init_sims(replace=True)

    return model


if __name__ == '__main__':
    from nltk.corpus import movie_reviews
    sentences = [list(s) for s in movie_reviews.sents()]
    print(len(sentences))

    model = word2vec(sentences)
    print(model.wv.similarity('he', 'she'))