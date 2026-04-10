import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "Natural language processing is interesting and useful."

# Tokenize
words = nltk.word_tokenize(text)

# POS tagging
pos_tags = nltk.pos_tag(words)

print(pos_tags)