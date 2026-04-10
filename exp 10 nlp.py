def transformation_tagger(sentence):
    words = sentence.split()

    # Step 1: Initial tagging (default = NN)
    tags = ["NN" for _ in words]

    # Step 2: Apply transformation rules
    for i, word in enumerate(words):
        if word.lower() in ["is", "am", "are", "was"]:
            tags[i] = "VB"

        if word.endswith("ing"):
            tags[i] = "VBG"

        if word.lower() == "the":
            tags[i] = "DT"

        # Example contextual rule:
        if i > 0 and words[i-1].lower() == "the":
            tags[i] = "NN"

    return list(zip(words, tags))

# Example
print(transformation_tagger("The cat is running"))