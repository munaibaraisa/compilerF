tokens = ["id", "+", "id", "*", "id"]
pos = 0

def match(expected):
    global pos
    if pos < len(tokens) and tokens[pos] == expected:
        print(f"Matched: {expected}")
        pos += 1
        return True
    return False

def F():
    if match("id"):
        return "F"
    elif match("("):
        node = E()
        if not match(")"):
            print("Error: missing )")
        return node

def T():
    node = F()
    while pos < len(tokens) and tokens[pos] == "*":
        match("*")
        right = F()
        node = f"({node} * {right})"
    return node

def E():
    node = T()
    while pos < len(tokens) and tokens[pos] == "+":
        match("+")
        right = T()
        node = f"({node} + {right})"
    return node

parse_tree = E()
if pos == len(tokens):
    print("Parsing successful!")
    print("Top-Down Parse Tree:", parse_tree)
else:
    print("Parsing failed.")
