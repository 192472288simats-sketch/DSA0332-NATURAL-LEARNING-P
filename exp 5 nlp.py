import nltk
from nltk.stem import PorterStemmer

# Initialize stemmer
ps = PorterStemmer()

words = ["running", "jumps", "easily", "flying", "cats"]

for word in words:
    print(word, "->", ps.stem(word))