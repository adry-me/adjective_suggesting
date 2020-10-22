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
import nlp.encoder as encoder
import numpy as np


def collect_adjectives(path):
    objects = Adjective.objects.all()
    with open(f'{path}/adj.txt', 'w') as f:
        for obj in objects:
            f.write(f'{obj.word}\n')


def check_adjectives(line, size=2, adj=None):
    result = []
    words = line.split()
    for i, word in enumerate(words):
        if (adj is not None and word in adj) or\
           (adj is None and len(Adjective.objects.filter(word=word)) > 0):
            word_result = []
            for idx in range(i - size, i + size + 1):
                if idx < 0:
                    word_result.append('')
                elif idx >= len(words):
                    word_result.append('')
                else:
                    word_result.append(words[idx])
            result.append(word_result)

    return result


# from SuggestAdjectives.collect_adjectives import *
def main(path, suffix='_mod', size=2):
    with open(f'{path}/adj.txt') as f:
        adj = list(map(lambda x: x[:-1], f.readlines()))

    authors = [d for d in os.listdir(f'{path}')
               if os.path.isdir(f'{path}/{d}')
               and d[0] not in ['.', '_']]
    for author in authors:
        X = []
        y_words = []
        y = []

        for fname in [f'{path}/{author}/{fn}' for fn in os.listdir(f'{path}/{author}') if suffix in fn]:
            with open(fname) as f:
                for line in f.readlines():
                    results = check_adjectives(line.rstrip(), size, adj)
                    if len(results) > 0:
                        for res in results:
                            vec = []
                            for i, word in enumerate(res):
                                if word == '':
                                    continue

                                index = encoder.decode(word, author)

                                if index != -1:
                                    if i == size:
                                        if word not in y_words:
                                            y_words.append(word)
                                        y.append([y_words.index(word)])
                                    else:
                                        vec.append(index)
                            while len(vec) < size * 2:
                                vec.append(0)
                            X.append(vec)

        with open(f'{path}/{author}/{len(y_words)}-adjectives.bytes', 'wb') as f:
            for word in y_words:
                f.write(bytes(f'{word} ', encoding='utf-8'))
        X_array = np.asarray(X, dtype=np.int)
        y_array = np.asarray(y, dtype=np.int)

        np.save(f'{path}/X_{author}_size_{size}.npy', X_array)
        np.save(f'{path}/y_{author}_size_{size}.npy', y_array)


if __name__ == '__main__':
    for s in range(2, 6):
        main('../data', size=s)
        print(s)
