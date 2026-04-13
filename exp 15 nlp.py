grammar = {
    "S": [("NP VP", 1.0)],
    "NP": [("John", 0.5), ("Mary", 0.5)],
    "VP": [("runs", 0.6), ("eats", 0.4)]
}

def pcfg_parse(sentence):
    words = sentence.split()
    prob = 1.0
    
    if words[0] in ["John", "Mary"]:
        prob *= 0.5
    if words[1] == "runs":
        prob *= 0.6
    elif words[1] == "eats":
        prob *= 0.4
    
    return prob

sentence = "John runs"
print("Probability:", pcfg_parse(sentence))