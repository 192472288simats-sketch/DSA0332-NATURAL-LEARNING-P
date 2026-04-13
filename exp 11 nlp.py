grammar = {
    "S": ["aSb", ""]
}

def parse(s, symbol):
    if symbol == "":
        return s == ""
    
    for production in grammar.get(symbol, []):
        if production == "":
            if s == "":
                return True
        elif len(s) > 0 and production[0] == s[0]:
            if parse(s[1:], production[1:]):
                return True
    return False

string = "aaabbb"
print("Accepted" if parse(string, "S") else "Rejected")