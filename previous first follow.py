grammar = {
    "E": [["T","E'"]],
    "E'": [["+","T","E'"], ["ε"]],
    "T": [["F","T'"]],
    "T'": [["*","F","T'"], ["ε"]],
    "F": [["(","E",")"], ["id"]]
}

first = {}
follow = {}

# Initialize
for nt in grammar:
    first[nt] = set()
    follow[nt] = set()

follow["E"] = {"$"}  # start symbol

# FIRST sets (simple manual filling for this small grammar)
first["F"] = {"(", "id"}
first["T'"] = {"*", "ε"}
first["T"] = {"(", "id"}
first["E'"] = {"+", "ε"}
first["E"] = {"(", "id"}

# FOLLOW sets (simple manual filling)
follow["E"] = {")", "$"}
follow["E'"] = {")", "$"}
follow["T"] = {"+", ")", "$"}
follow["T'"] = {"+", ")", "$"}
follow["F"] = {"*", "+", ")", "$"}

# Print
print("FIRST sets:")
for k,v in first.items():
    print(f"{k}: {v}")

print("\nFOLLOW sets:")
for k,v in follow.items():
    print(f"{k}: {v}")
