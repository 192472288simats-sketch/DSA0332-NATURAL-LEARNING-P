class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def parse_sentence():
    root = Node("S")
    
    np = Node("NP")
    vp = Node("VP")
    
    np.children.append(Node("John"))
    vp.children.append(Node("runs"))
    
    root.children = [np, vp]
    return root

def print_tree(node, level=0):
    print(" " * level + node.value)
    for child in node.children:
        print_tree(child, level + 2)

tree = parse_sentence()
print_tree(tree)