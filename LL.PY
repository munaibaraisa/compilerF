from tabulate import tabulate

# Parsing Table
table = {
    "E": {"id": ["T","E'"], "(": ["T","E'"]},
    "E'": {"+": ["+","T","E'"], ")": ["ε"], "$": ["ε"]},
    "T": {"id": ["F","T'"], "(": ["F","T'"]},
    "T'": {"+": ["ε"], "*": ["*","F","T'"], ")": ["ε"], "$": ["ε"]},
    "F": {"id": ["id"], "(": ["(","E",")"]}
}

# Grammar for display
grammar = [
    ("E", ["T","E'"]), ("E'", ["+","T","E'"]), ("E'", ["ε"]),
    ("T", ["F","T'"]), ("T'", ["*","F","T'"]), ("T'", ["ε"]),
    ("F", ["id"]), ("F", ["(","E",")"])
]

def show_grammar():
    print("\nGrammar:")
    print(tabulate([[i+1, f"{lhs} → {' '.join(rhs)}"] for i,(lhs,rhs) in enumerate(grammar)],
                   headers=["No.","Production"], tablefmt="fancy_grid"))

def parse(tokens):
    stack = ["$","E"]
    tokens.append("$")
    steps = []
    index = 0

    while stack:
        top = stack[-1]
        tok = tokens[index]

        if top == tok == "$":
            steps.append([list(stack), tokens[index:], "Accept ✅"])
            break
        elif top == tok:
            stack.pop(); index += 1
            steps.append([list(stack), tokens[index:], f"Match {tok}"])
        elif top in table and tok in table[top]:
            stack.pop()
            prod = table[top][tok]
            if prod != ["ε"]: stack += reversed(prod)
            steps.append([list(stack), tokens[index:], f"{top} → {' '.join(prod)}"])
        else:
            steps.append([list(stack), tokens[index:], f"Error ❌ at {tok}"])
            break

    print(tabulate([[i+1]+row for i,row in enumerate(steps)],
                   headers=["Step","Stack","Input","Action"], tablefmt="fancy_grid"))

# ---------------- Example ----------------
show_grammar()

tokens_list = [
    ["id","+","id","*","id"],
    ["(","id","+","id",")","*","id"],
    ["id","*","+","id"]
]

for i,toks in enumerate(tokens_list,1):
    print(f"\n--- Parsing tokens{i} ---")
    parse(toks.copy())
