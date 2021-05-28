import spacy
import string

def spacy_token_to_str(spacy_res):
    res = ""
    for i in spacy_res:
        res += str(i) + " "
    return res[:-1]

def remove_punc(text):
    """
    Uses python to remove all punctuation from a string and returns the new string
    """
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text):
    """
    Uses spacy to remove all stopwords from a string and returns the new string
    """
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(text)
    text_without_stop_words = [t.text for t in doc if not t.is_stop]
    return spacy_token_to_str(text_without_stop_words)

#with open("context.txt") as f:
#    context = f.readlines()
#with open('remove_punc.txt', 'w') as f:
#    for ent in context:
#        f.write("%s" % remove_punc(ent))