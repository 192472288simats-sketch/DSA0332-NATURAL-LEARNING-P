import random
from collections import defaultdict

def build_bigram_model(text):
    words = text.split()
    bigrams = defaultdict(list)

    for i in range(len(words) - 1):
        bigrams[words[i]].append(words[i + 1])

    return bigrams

def generate_text(model, start_word, length=10):
    word = start_word
    result = [word]

    for _ in range(length - 1):
        if word in model:
            word = random.choice(model[word])
            result.append(word)
        else:
            break

    return ' '.join(result)

# Example usage
text = "I love natural language processing and I love machine learning"
model = build_bigram_model(text)

print(generate_text(model, "I", 10))