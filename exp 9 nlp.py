import re

def rule_based_tagger(sentence):
    words = sentence.split()
    tagged = []

    for word in words:
        if re.match(r'.*ing$', word):
            tag = 'VBG'  # gerund verb
        elif re.match(r'.*ed$', word):
            tag = 'VBD'  # past tense verb
        elif re.match(r'.*ly$', word):
            tag = 'RB'   # adverb
        elif re.match(r'.*ous$', word):
            tag = 'JJ'   # adjective
        elif re.match(r'^[A-Z].*', word):
            tag = 'NNP'  # proper noun
        else:
            tag = 'NN'   # default noun

        tagged.append((word, tag))

    return tagged

# Example
print(rule_based_tagger("Ram is running quickly"))