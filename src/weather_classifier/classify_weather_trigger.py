from sentence_transformers import SentenceTransformer, util
import random
import tqdm

model = SentenceTransformer('paraphrase-distilroberta-base-v1')
def is_trigger_sentence_transformer(sents, triggers):
#Compute embedding for both lists
    embeddings1 = model.encode([sents], convert_to_tensor=True)
    embeddings2 = model.encode([triggers], convert_to_tensor=True)
    for item in embeddings1:
        cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
        if cosine_scores[0] > .7:
            return True
    # return cosine_scores[0] > .7
    return False
# def compute_accuracy(sents, trigs, is_trigger):
#     identified_trigger = 0
#     random.shuffle(sents)
#     for sent in tqdm(sents):
#         for trig in trigs:
#             if is_trigger(sent, trig):
#                 identified_trigger += 1
#                 break
#     return identified_trigger, identified_trigger/len(sents)
