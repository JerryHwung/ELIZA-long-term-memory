import re
# Generic responds for SVO structure
gSVO = [
    "I remember you told me that %1",
    "Oh, I know that %1",
]
# Generic respond for if a certain object doesn't have adj or adv
gS = [
    "Oh, your %1",
    "You mean %1"
]

def generateResp(list):
    for item in list:
        space  = ' '
        svo = (space.join(item))
        svo = re.sub(r"\bi\b", "you", svo)
        print(svo)
        for resp in gSVO:
            print(resp.replace("%1", svo))

