from transformers import pipeline
qa_nlp = pipeline("question-answering")

def handle_qa(context, explicit_question="Where is the weather?"):
    result = qa_nlp(context=context, question=explicit_question)
    answer = result["answer"]
    return answer

# TODO possible add more options