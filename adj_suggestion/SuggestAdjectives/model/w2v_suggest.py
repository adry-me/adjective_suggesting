import os
import gensim
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
from gensim import matutils
from gensim.models.keyedvectors import WordEmbeddingsKeyedVectors
from six import string_types
from numpy import dot, float32 as REAL, array, ndarray


_root_dir = os.path.abspath(os.path.dirname(__file__))
_size = 2
_embedding = 128
_authors = []
_word_objects = {}
_adjective_objects = {}
_w2v = {}


def most_similar(author, word):
    return _most_similar(_get_w2v(author), author, word)


def _get_w2v(author):
    if author not in _w2v:
        _w2v[author] = create_w2v(f'{_root_dir}/{author}/vectors.txt')
    return _w2v[author]


def _load_file(author):
    word_path = ''
    adj_path = ''
    for fname in os.listdir(f'{_root_dir}/{author}'):
        if 'word' in fname and author in fname:
            word_path = fname
        if 'adjectives' in fname and author in fname:
            adj_path = fname

    if word_path == '' or adj_path == '':
        return [], []

    with open(f'{_root_dir}/{author}/{word_path}', 'rb') as f:
        words = f.read().decode(encoding='utf-8').split()

    with open(f'{_root_dir}/{author}/{adj_path}', 'rb') as f:
        adjs = f.read().decode(encoding='utf-8').split()

    return words, adjs


def _initialize():
    for fname in os.listdir(_root_dir):
        if os.path.isdir(f'{_root_dir}/{fname}') and fname[0] not in ['.', '_']:
            _authors.append(fname)
            words, adjs = _load_file(fname)
            _word_objects[fname] = words
            _adjective_objects[fname] = adjs


_initialize()


def _most_similar(self: WordEmbeddingsKeyedVectors, author, input_word):
    topn = 10

    positive = [input_word]

    self.init_sims()

    # add weights for each word, if not already present; default to 1.0 for positive and -1.0 for negative words
    positive = [
        (word, 1.0) if isinstance(word, string_types + (ndarray,)) else word
        for word in positive
    ]

    # compute the weighted average of all words
    all_words, mean = set(), []
    for word, weight in positive:
        if isinstance(word, ndarray):
            mean.append(weight * word)
        else:
            mean.append(weight * self.word_vec(word, use_norm=True))
            index = encode_adj(word, author)

            if index >= 0:
                all_words.add(index)
    if not mean:
        raise ValueError("cannot compute similarity with no input")
    mean = matutils.unitvec(array(mean).mean(axis=0)).astype(REAL)

    limited = self.vectors_norm
    dists = dot(limited, mean)

    if not topn:
        return dists
    best = matutils.argsort(dists, topn=topn + len(all_words), reverse=True)
    # ignore (don't return) words from the input
    result = [(sim, float(dists[sim])) for sim in best if sim not in all_words]

    adj_res = [
        (decode(r[0], author), r[1]) for r in result
        if encode_adj(decode(r[0], author), author) >= 0
    ]

    return adj_res[:topn]


def create_vector(model, author):
    word_object = _word_objects[author]
    out_path = f'{_root_dir}/{author}/vectors.txt'

    with open(out_path, 'w') as f:
        f.write('{} {}\n'.format(len(word_object), _embedding))
        vectors = model.get_weights()[0]
        for i, word in enumerate(word_object):
            str_vec = ' '.join(map(str, list(vectors[i + 1, :])))
            f.write('{} {}\n'.format(word, str_vec))


def set_model(author):
    vocab = len(_word_objects[author])
    adj = len(_adjective_objects[author])

    model = Sequential([
        Embedding(vocab, _embedding, input_length=_size * 2, name="embedding"),
        GlobalAveragePooling1D(),
        Dense(adj, activation='softmax')
    ])

    latest = tf.train.latest_checkpoint(f'{_root_dir}/{author}')
    model.load_weights(latest)

    return model


def create_w2v(vector_path):
    w2v_gen = gensim.models.KeyedVectors.load_word2vec_format(vector_path, binary=False)
    return w2v_gen


def encode(word, author):
    if word not in _word_objects[author]:
        return -1

    return _word_objects[author].index(word)


def decode(index, author):
    return _word_objects[author][index]


def encode_adj(word, author):
    if word not in _adjective_objects[author]:
        return -1

    return _adjective_objects[author].index(word)

def decode_adj(index, author):
    return _adjective_objects[author][index]


if __name__ == '__main__':
    print(most_similar('Tolstoy', 'kind'))