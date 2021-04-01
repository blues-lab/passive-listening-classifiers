from spacy_NER import find_most_recent_LOCs
from handle_qa_multiple_option import handle_qa
import spacy
def spacy_token_to_str(spacy_res):
    res = ""
    for i in spacy_res:
        res += str(i)
    return res
nlp = spacy.load('en_core_web_lg')

def compute_loc(context):
    locs = find_most_recent_LOCs(context)
    print("Original", context, locs)
    if len(locs) >= 2:
        qa_answer = handle_qa("".join(context))
        qa_answer_nlp = nlp(qa_answer)
        print("Qa answer", qa_answer)
        max_similarity = 0.0
        best_loc = None
        for item in locs:
            if not item: continue
            nlp_loc = nlp(str(item))
            sim = qa_answer_nlp.similarity(nlp_loc)
            if sim > max_similarity:
                best_loc = str(item)
                max_similarity = sim

        # maximal_result = max(locs, key=lambda loc: nlp(loc).similarity(qa_answer_nlp))
        print("Selected Best Loc", best_loc)
        return best_loc
    else:
        return locs[0]

if __name__ == "__main__":
    context = ["How is like to be in Berkeley", "Last few weeks It's been very hot","I think we should check the weather in San Jose instead"]
    compute_loc(context)
