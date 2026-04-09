def pluralize(noun):
    if noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    else:
        return noun + 's'


# Test
words = ["cat", "bus", "box", "baby", "brush"]
for w in words:
    print(w, "->", pluralize(w))