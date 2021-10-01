#
import spacy
import truecase

# with open("/context.txt") as f:
#    context = f.readlines()


def most_recent_GPE(sentence, nlp):
    """
    Return the most recent Geopolitical Entity (GPE) in string of lowercase sentence(s)
    """
    truecased_sentence = truecase.get_true_case(sentence.lower())
    most_recent_GPE = ""
    for ent in nlp(truecased_sentence).ents:
        if ent.label_ == "GPE":
            most_recent_GPE = ent
    return most_recent_GPE


def find_most_recent_GPEs(context):
    """
    Returns a list of the most recent geopolitical entity (GPE) mentioned in set of lowercase sentences
    who are truecased back to having case. Uses en_core_web_lg spacy pipeline
    """
    nlp = spacy.load("en_core_web_lg")
    most_recent_GPEs = []
    for i in range(len(context)):
        st = truecase.get_true_case(context[i].lower())
        print("\n" + st)
        GPE = most_recent_GPE(st, nlp)
        print("===> Most recently named GPE:", GPE)
        print()
        most_recent_GPEs.append(GPE)
    return most_recent_GPEs


def most_recent_LOC(sentence, nlp_wk):
    """
    Return the most recent location (LOC) in string of lowercase sentence(s)
    """
    truecased_sentence = truecase.get_true_case(sentence.lower())
    most_recent_LOC = ""
    for ent in nlp_wk(truecased_sentence).ents:
        if ent.label_ == "LOC":
            most_recent_LOC = ent
    return most_recent_LOC


def find_most_recent_LOCs(context):
    """
    Returns a list of the most recent location (LOC) mentioned in set of lowercase sentences
    who are truecased back to having case. Uses xx_ent_wiki_sm spacy pipeline
    """
    nlp_wk = spacy.load("xx_ent_wiki_sm")
    most_recent_LOCs = []
    for i in range(len(context)):
        st = truecase.get_true_case(context[i].lower())
        print("\n" + st)
        location = most_recent_LOC(st, nlp_wk)
        print("===> Most recently named LOC:", location)
        print()
        most_recent_LOCs.append(location)
    return most_recent_LOCs


nlp = spacy.load("en_core_web_lg")


def two_most_frequent_GPEs(sentence):
    """
    Return the two most frequent Geopolitical Entities (GPEs) in string of lowercase sentence(s) along with their frequencies
    Sample outputs can be:
        [("New York City", 2), ("London", 1)] or
        [("Portland", 1)] or
        []
    """
    truecased_sentence = truecase.get_true_case(sentence.lower())
    GPEs = {}
    for ent in nlp(truecased_sentence).ents:
        if ent.label_ == "GPE":
            GPEs[str(ent)] = GPEs.get(str(ent), 0) + 1
    if not GPEs:
        return []
    if len(GPEs) == 1:
        return [(list(GPEs.keys())[0], list(GPEs.values())[0])]
    k = sorted(list(GPEs.keys()), key=lambda x: GPEs[x])[-2:]
    v = sorted(list(GPEs.values()))[-2:]
    return [(k[1], v[1]), (k[0], v[0])]


def find_two_most_frequent_GPEs(context):
    """
    Returns a list of the tuple of the two most frequent geopolitical entities (GPEs) mentioned in set of lowercase sentences
    who are truecased back to having case. Tuple contains GPE and its frequency. Uses en_core_web_lg spacy pipeline
    """
    most_frequent_GPEs = []
    for i in range(len(context)):
        st = truecase.get_true_case(context[i].lower())
        print("\n" + st)
        GPEs = two_most_frequent_GPEs(st)
        print("===> Most frequently named GPEs:", GPEs)
        print()
        most_frequent_GPEs.append(GPEs)
    return most_frequent_GPEs


nlp_wk = spacy.load("xx_ent_wiki_sm")


def two_most_frequent_LOCs(sentence):
    """
    Return the two most frequent locations (LOCs) in string of lowercase sentence(s) along with their frequencies
    Sample outputs can be:
        [("New York City", 2), ("London", 1)] or
        [("Portland", 1)] or
        []
    """
    truecased_sentence = truecase.get_true_case(sentence.lower())
    LOCs = {}
    for ent in nlp_wk(truecased_sentence).ents:
        if ent.label_ == "LOC":
            LOCs[str(ent)] = LOCs.get(str(ent), 0) + 1
    if not LOCs:
        return []
    if len(LOCs) == 1:
        return [(list(LOCs.keys())[0], list(LOCs.values())[0])]
    k = sorted(list(LOCs.keys()), key=lambda x: LOCs[x])[-2:]
    v = sorted(list(LOCs.values()))[-2:]
    return [(k[1], v[1]), (k[0], v[0])]


def find_two_most_frequent_LOCs(context):
    """
    Returns a list of the tuple of the two most frequent locations (LOCs) mentioned in set of lowercase sentences
    who are truecased back to having case. Tuple contains LOC and its frequency. Uses en_core_web_lg spacy pipeline
    """
    most_frequent_LOCs = []
    for i in range(len(context)):
        st = truecase.get_true_case(context[i].lower())
        print("\n" + st)
        LOCs = two_most_frequent_LOCs(st)
        print("===> Most frequently named LOCs:", LOCs)
        print()
        most_frequent_LOCs.append(LOCs)
    return most_frequent_LOCs


def all_LOCs_with_frequencies(sentence):
    """
    Return the two most frequent locations (LOCs) in string of lowercase sentence(s) along with their frequencies
    Sample outputs can be:
        [("New York City", 2), ("London", 1)] or
        [("Portland", 1)] or
        []
    """
    truecased_sentence = truecase.get_true_case(sentence.lower())
    LOCs = {}
    for ent in nlp_wk(truecased_sentence).ents:
        if ent.label_ == "LOC":
            LOCs[str(ent)] = LOCs.get(str(ent), 0) + 1
    if not LOCs:
        return []
    return list(LOCs.items())


# with open('most_recent.txt', 'w') as f:
#     for ent in find_two_most_frequent_GPEs(context):
#     #for ent in find_most_recent_LOCs(context):
#         f.write("%s\n" % ent)
