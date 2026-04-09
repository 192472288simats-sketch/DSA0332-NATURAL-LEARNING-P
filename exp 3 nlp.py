import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The cats are running in the garden"

tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

print("Tokens:", tokens)
print("POS Tags:", pos_tags)