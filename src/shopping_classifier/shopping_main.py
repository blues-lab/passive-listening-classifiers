import os
import pickle
import sys
from fuzzywuzzy import process
import numpy as np
import pandas as pd
import spacy
import tensorflow as tf
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import regularizers
from tensorflow.keras.layers import (
    Input,
    Dense,
    Dropout,
    Concatenate,
    Flatten,
    Conv2D,
)
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

from models import InferSent

np.random.seed(3252)
PATH = (os.path.dirname(os.path.abspath(__file__))) + "/"

def get_doc2vec(text, model, verbose=False):
    emb = model.encode(text, verbose=verbose)
    return emb


def find_shopping_item(text):
    model = torch.load(PATH + "infraset_model.torch")
    model.eval()
    label_encoder = pickle.load(open(PATH + "label_encoding.pkl", "rb"))

    def get_labels_decoded(arr):
        return label_encoder.inverse_transform(arr)
    def cosine(u, v):
        return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    en_nlp = spacy.load("en_core_web_sm")
    doc = en_nlp(text)
    sentence = next(doc.sents)
    predicted_item = set()
    productlisting = list()
    with open(PATH + "food.txt") as my_file:
        for line in my_file:
            productlisting.append(str(line).strip())
    for word in sentence:
        if "obj" in word.dep_ or "conj" in word.dep_:
            if cosine( model.encode(["shopping market or grocery store"])[0],
                model.encode([str(word)])[0],
            ) < cosine(
                model.encode(["food or item"])[0], model.encode([str(word)])[0]
            ):
                # print(word)
                temp = word
                if prev[1] == "amod":
                    # This is used for compound words
                    word = prev[0]+ " " + word
                # checks cosine similarity
                cosSim = cosine(
                    model.encode(["grocery item"])[0],
                    model.encode([str(word)])[0],
                )
                print(cosSim) 
                curwordvec = en_nlp(str(temp))
                if cosSim > 0.35:
                    predicted_item.add(word)
                else:
                    for product in productlisting:
                        if en_nlp(product).similarity(curwordvec) > 0.8:
                            predicted_item.add(word)
                            break
        prev = (word, word.dep_)
    return list(predicted_item)


if __name__ == "__main__":
    res = find_shopping_item("We ran out of juice and soda")
    print(res)