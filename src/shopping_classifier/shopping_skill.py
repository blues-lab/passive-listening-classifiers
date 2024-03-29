
import pickle
import tensorflow as tf
import numpy as np
import torch
import os
from shopping_classifier.shopping_main import find_shopping_item

basedir = os.path.abspath(os.path.dirname(__file__))

class ShoppingSkill(object):
    skill_name = "Shopping"
    model_name = "ffcc_keras_model"
    label_encoder_name = "label_encoding.pkl"
    infraset_model_name = "infraset_model.torch"

    def __init__(self):
        # super().__init__()
        self.ffcc = None
        self.label_encoder = None
        self.infraset_model = None
        self.init_models() # TODO move this out of init
        
    def init_models(self):
        self.ffcc = tf.keras.models.load_model(os.path.join(basedir,self.model_name), compile = False)
        self.label_encoder = pickle.load(open(os.path.join(basedir, self.label_encoder_name), 'rb'))
        self.infraset_model = torch.load(os.path.join(basedir, self.infraset_model_name))
        self.infraset_model.eval()

    def classify(self, text, cutoff=0.0):
        X = self.get_doc2vec([text])
        predictions = self.ffcc.predict(X)
        predicted_labels = self.get_labels_decoded(np.argmax(predictions, axis=1))  # each integer is [0, 0, 0,1]
        prob = np.max(predictions, axis=1)  # each integer is [0, 0, 0,1]
        if prob < cutoff:
            predicted_labels[0] = 'oos'  # since only one item

        return predicted_labels[0], prob[0]
    
    def get_labels_decoded(self, arr):
        return self.label_encoder.inverse_transform(arr)

    def get_doc2vec(self, text, verbose=False):
        return self.infraset_model.encode(text, verbose=verbose)

    def find_shopping_item(self, text):
        return find_shopping_item(text)


