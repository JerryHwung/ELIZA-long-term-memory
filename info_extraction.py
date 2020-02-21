# The idea of this piece of code is based on:
# https://github.com/NSchrading/intro-spacy-nlp/blob/master/subject_object_extraction.py

import spacy

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
    #print(subs)
    return subs
# Get all objects
def getObjs(NPs):
    objs = [span for span in NPs if span.root.dep_ in OBJECTS]
    # Adding objects after a conjunction
    objs.extend([span for span in NPs if span.root.dep_ == "conj" and span.root.pos_ == "PROPN"])
    objs.extend([span for span in NPs if span.root.dep_ == "conj" and span.root.pos_ == "NOUN"])
    #print(objs)
    return objs
# Getting noun phrase (NP)
def getNP(doc):
    # the chunks in the list are Span
    nounChunks = [chunk for chunk in doc.noun_chunks]
    #print("NPs: ", nounChunks)
    return nounChunks
# Getting names from the noun chunks
def getAttr(doc):
    attr = [token.text for token in doc if token.dep_ == "attr"]
    print("names: ", attr)
# Get adjective
def getAdj(doc):
    adjs = [token.lemma_ for token in doc if token.pos_ == "ADJ"]
    return adjs
#My car is red and big
# find SVOs
def findSVO(input):
    doc = nlp(input)
    for token in doc:
        print(token.pos_, token.dep_)
    svos = []
    verbs = [token for token in doc if token.pos_ == "VERB" and token.dep_ != "aux"]
    if verbs == []:
        verbs = [token for token in doc if token.pos_ == "AUX" and token.dep_ == "ROOT"]
    NPs = getNP(doc)
    subs = getSubs(NPs)
    objs = getObjs(NPs)
    adjs = getAdj(doc)
    # This if statement is to solve SVO conj SVO format
    if len(subs) > 1 and len(verbs) > 1:
        for i in range(len(subs)):
            svos.append((subs[i].lower_, verbs[i].lower_, objs[i].lower_))

        if len(svos) > 2:
            svos = [()]
            objs = []
        return svos, objs
    # This handles sentence with only subject and adjectives
    elif adjs != []:
        keylist = []
        for v in verbs:
            verbNegated = isNegated(doc)
            for sub in subs:
                key = sub.lower_
                keylist.append(key)
                for adj in adjs:
                    svos.append((sub.lower_, v.lower_ + " not" if verbNegated else v.lower_, adj))
        return svos, keylist
    else:
        for v in verbs:
            verbNegated = isNegated(doc)
            for sub in subs:
                for obj in objs:
                    svos.append((sub.lower_, "don't " + v.lower_ if verbNegated else v.lower_, obj.lower_))

        if len(svos) > 2:
            svos = [()]
            objs = []
        return svos, objs
# find SVs (still in progress)
def findSV(input):
    doc = nlp(input)
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

while True:
    txt = input("> ")
    print(findSVO(txt))