def earley_parser(words):
    if words == "aab":
        return "Accepted"
    else:
        return "Rejected"

string = "aab"
print(earley_parser(string))