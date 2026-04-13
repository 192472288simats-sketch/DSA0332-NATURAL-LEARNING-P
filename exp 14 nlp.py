def check_agreement(sentence):
    words = sentence.split()
    
    subject = words[0]
    verb = words[1]
    
    if subject in ["he", "she", "it"] and verb.endswith("s"):
        return "Correct"
    elif subject in ["I", "we", "they"] and not verb.endswith("s"):
        return "Correct"
    else:
        return "Incorrect"

sentence = "he runs"
print(check_agreement(sentence))