from gensim.models.word2vex import Word2Vec


def lines_to_sentences(lines):
    return list(map(str.split, lines))


def word2vec(lines):
    model = Word2Vec(lines)
    model.init_sims(replace=True)

    return model