from gensim.models.word2vec import Word2Vec
import nltk


def lines_to_sentences(lines):
    return list(map(str.split, lines))


def word2vec(lines):
    model = Word2Vec(lines)
    model.init_sims(replace=True)

    return model


def analyze_text(text):
    adj_list = []
    sentences = nltk.sent_tokenize(text)

    for sentence in sentences:
        for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if pos == 'JJ':
                adj_list.append(word)

    count = nltk.Counter(adj_list)

    return adj_list, count


if __name__ == '__main__':
    with open('data/P_P_mod.txt') as f:
        adj_list, count = analyze_text(f.read())

    print(adj_list)
    print(count)