from sentence_transformers import SentenceTransformer, util
import random
import tqdm
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

with open("src/weather_classifier/triggers.txt") as f:
    triggers = f.readlines()
    triggers = [model.encode([trigger], convert_to_tensor=True) for trigger in triggers]

def is_trigger_sentence_transformer(sents):
    embeddings1 = model.encode([sents], convert_to_tensor=True)
    for trigger in triggers:
        cosine_scores = util.pytorch_cos_sim(embeddings1, trigger)
        print(cosine_scores)
        if cosine_scores[0] >= .6:
            return True
    return False