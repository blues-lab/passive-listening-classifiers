from .spacy_NER import all_LOCs_with_frequencies
from .handle_qa_multiple_option import handle_qa
from .remove_punc_and_stopwords import remove_punc
import spacy
import pandas as pd

nlp = spacy.load("en_core_web_lg")


def compute_loc(context):
    if type(context) == list:
        context = " ".join([remove_punc(text) for text in context])
    else:
        context = remove_punc(context)
    locs = all_LOCs_with_frequencies(context)
    print("Original", context, locs)
    if len(locs) >= 2:
        qa_answer = handle_qa(context)
        qa_answer_nlp = nlp(qa_answer)
        print("Qa answer", qa_answer)
        max_similarity = 0.0
        best_loc = None
        for item, freq in locs:
            nlp_loc = nlp(str(item))
            sim = qa_answer_nlp.similarity(nlp_loc)
            if sim > max_similarity:
                best_loc = str(item)
                max_similarity = sim

        # maximal_result = max(locs, key=lambda loc: nlp(loc).similarity(qa_answer_nlp))
        print("Selected Best Loc ==>", best_loc)
        return best_loc
    elif len(locs) == 1:
        return locs[0][0]
    else:
        return ""


if __name__ == "__main__":
    # context = ["How is like to be in Berkeley", "Last few weeks it's been very hot","I think we should check the weather in San Jose instead"]
    # print(compute_loc(context))

    data = pd.read_csv("text_generation/megatron11b_examples.csv")
    for text in data.iloc[:, 0]:
        print(compute_loc(text))
