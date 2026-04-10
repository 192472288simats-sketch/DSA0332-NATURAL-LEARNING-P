from collections import defaultdict, Counter

# Training data (word, tag)
train_data = [
    ("I", "PRON"), ("love", "VERB"), ("NLP", "NOUN"),
    ("I", "PRON"), ("love", "VERB"), ("AI", "NOUN"),
    ("AI", "NOUN"), ("is", "VERB"), ("fun", "ADJ")
]

# Build probability model P(tag|word)
word_tag_freq = defaultdict(Counter)

for word, tag in train_data:
    word_tag_freq[word][tag] += 1

def stochastic_tagger(sentence):
    words = sentence.split()
    tagged = []

    for word in words:
        if word in word_tag_freq:
            tag = word_tag_freq[word].most_common(1)[0][0]
        else:
            tag = "UNK"
        tagged.append((word, tag))

    return tagged

# Example
print(stochastic_tagger("I love AI"))