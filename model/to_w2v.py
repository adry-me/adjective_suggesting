import os
import gensim
import tensorflow as tf
from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import Activation, Dense, Embedding, GlobalAveragePooling1D


def to_w2v(cp_path, out_path):
    model = Sequential([
        Embedding(vocab_size, embedding_dim, name="embedding"),
        GlobalAveragePooling1D(),
        Dense(adjective_size, activation='softmax')
    ])
