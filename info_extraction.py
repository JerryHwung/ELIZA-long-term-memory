import spacy
import resp
nlp = spacy.load("en_core_web_sm")

# declare lists of dependencies of subjects and objects
SUBJECTS = ["nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl"]
OBJECTS = ["dobj", "dative", "attr", "oprd"]
# Find SVO(Subject-Verb-Object) of a sentence
def isNegated(doc):
    for tok in doc:
        if tok.dep_ == "neg":
            return True
    return False

# Get all subjects
def getSubs(NPs):
    subs = [span for span in NPs if span.root.dep_ in SUBJECTS and span.root.pos_ != "DET"]
    print(subs)
    return subs
# Get all objects
def getObjs(NPs):
    objs = [span for span in NPs if span.root.dep_ in OBJECTS]
    # Adding objects after a conjunction
    objs.extend([span for span in NPs if span.root.dep_ == "conj" and span.root.pos_ == "NOUN"])
    print(objs)
    return objs
# Getting noun phrase (NP)
def getNP(doc):
    # the chunks in the list are Span
    nounChunks = [chunk for chunk in doc.noun_chunks]
    print("NPs: ", nounChunks)
    return nounChunks
# Getting names from the noun chunks
def getAttr(doc):
    attr = [token.text for token in doc if token.dep_ == "attr"]
    print("names: ", attr)
# Get adjective
def getAdj(doc):
    adjs = [token.lemma_ for token in doc if token.pos_ == "ADJ"]
    print("Adjectives: ", adjs)

# find SVOs
def findSVO(doc):
    svos = []
    verbs = [token for token in doc if token.pos_ == "VERB" and token.dep_ != "aux"]
    if verbs == []:
        verbs = [token for token in doc if token.pos_ == "AUX" and token.dep_ == "ROOT"]
    print(verbs)
    NPs = getNP(doc)
    subs = getSubs(NPs)
    objs = getObjs(NPs)
    for v in verbs:
        verbNegated = isNegated(doc)
        for sub in subs:
            for obj in objs:
                svos.append((sub.lower_, "!" + v.lower_ if verbNegated else v.lower_, obj.lower_))
    return svos
# find SVs
def findSV(doc):
    svs = []
    auxVerb = [token for token in doc if token.pos_ == "VERB" and token.dep_ == "aux"]
    mainVerbs = [token for token in doc if token.pos_ == "VERB" and token.dep_ != "aux"]
    adjvs = [token for token in doc if token.pos_ == "ADJ" or token.pos_ == "ADV"]
    attr = [token for token in doc if token.dep_ == "attr"]
    print(auxVerb)
    print(mainVerbs)
    NPs = getNP(doc)
    for aux in auxVerb:
        auxVerbNegated = isNegated(doc)
        for sub in NPs:
            if mainVerbs != []:
                for mainV in mainVerbs:
                    svs.append((sub.lower_, "!" + aux.lower_ if auxVerbNegated else aux.lower_, mainV.lower_))
            else :
                for adjv in adjvs:
                    svs.append((sub.lower_, "!" + aux.lower_ if auxVerbNegated else aux.lower_, adjv.lower_, attr))

    return svs

# gather the user input and gather the info
while True:
    doc = nlp(input("> "))
    # print out the pos and deps
    #for token in doc:
       #print("Token {} POS: {}, dep: {}, tag: {}".format(token.text, token.pos_, token.dep_, token.tag_))

    # get the input information
    list = findSVO(doc)
    resp.generateResp(list)