import nltk
nltk.download('movie_reviews')

from nltk.corpus import movie_reviews
sentences = [list(s) for s in movie_reviews.sents()]

from gensim.models.word2vec import Word2Vec

% % time
model = Word2Vec(sentences)

model.init_sims(replace=True)

model.wv.similarity('actor', 'actress')
model.wv.similarity('he', 'she')
model.wv.similarity('actor', 'she')
model.wv.most_similar("accident")
model.wv.most_similar(positive=['she', 'actor'], negative='actress', topn=1)

% % time
!wget - nc https: // raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt

import codecs
def read_data(filename):
    with codec.open(filename, encoding='utf-8', mode='r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[:1]    # except header
    return data
train_data = read_data('ratings_train.txt')

from konlpy.tag import Twitter
tagger = Twitter()

def tokenize(doc):
    return ['/'.join(t) for t in tagge.pos(doc, norm=True, stem=True)]
train_docs = [row[1] for row in train_data]


#% % time
#sentences = [tokenize(d) for d in train_docs]
#from gensim.models import word2vec
#% % time
#model = word2vec.Word2Vec(sentences)
#model.init_sims(replace=True)

#model.wv.similarity(*tokenize(u''))