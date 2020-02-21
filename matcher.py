import spacy

# load module for NER
nlp = spacy.load("en_core_web_sm")

def process_text(str):
    # process the text and store as a Doc
    doc = nlp(str)

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

process_text("I will be back")