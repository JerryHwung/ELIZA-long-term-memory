# Generic responds for SVO structure
gSVO = [
    "I remember you told me that %1. ",
    "Oh, I know that %1. ",
]
# Generic respond for if a certain object doesn't have adj or adv
gS = [
    "Oh, your %1. ",
    "You mean %1. "
]

gReflections = {
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you"
}

def generateResp(input):
    result = []
    for item in input:
        # change to list format
        words = list(item)
        print(words)
        dict = gReflections
        keys = dict.keys();
        for i in range(0, len(words)):
            if words[i] in keys:
                words[i] = dict[words[i]]
        fact = (' '.join(words))
        for resp in gSVO:
            result.append(resp.replace("%1", fact))
    return result