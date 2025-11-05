# Super simple rightmost derivation (no recursion)

# Grammar: S -> SS+ | SS* | a
grammar = {
    "S": ["SS+", "SS*", "a"]
}

# Target string
target = "aa+a*"

# Start with S
current = "S"
steps = [current]

print("Grammar: S -> SS+ | SS* | a")
print(f"Target string: {target}\n")

# Simple loop to simulate rightmost derivation
while current != target:
    # Find rightmost 'S'
    index = current.rfind("S")  # rightmost S
    if index == -1:
        print("No derivation possible")
        break
    
    # Simple manual rule application (for this example)
    # If remaining string starts with 'aa+', choose SS* for last
    if len(current) < len(target):
        if current == "S":
            current = current.replace("S", "SS*", 1)
        elif current.count("S") > 1:
            current = current.replace("S", "SS+", 1)
        else:
            current = current.replace("S", "a", 1)
    steps.append(current)

# Print derivation steps
print("Rightmost derivation steps:")
for i, step in enumerate(steps):
    print(f"Step {i}: {step}")
