In order to make this code work you need:

1. Python 3.7.2
2. pip (for installing spaCy)
3. A model package for spaCy use($python -m spacy download en_core_web_sm) to download into path

After setting things up, just run the controller.py will intially start
the chatbot.

After entering a new name at the intro, you might get an error message,
that's fine because there are no file to load. The chatbot will proceed.

Do remember the chatbot will only save the memory if the user type quit in input

Please keep the sentence simple and only contain one clause to test the memory
mechanism. So far it can recognised simple SVO, SVOO, S(ADJ),S(ADJ*2), SVOSVO.

Terminology
S = Subject O = Object V = Verb ADJ = Adjective
