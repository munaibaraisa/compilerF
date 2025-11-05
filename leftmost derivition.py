# Super simple leftmost derivation (no recursion)

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

# Loop to simulate leftmost derivation
while current != target:
    # Find leftmost 'S'
    index = current.find("S")  # leftmost S
    if index == -1:
        print("No derivation possible")
        break
    
    # Simple manual rule application
    # Choose production based on example target
    if current == "S":
        current = current.replace("S", "SS+", 1)
    elif current.count("S") > 1:
        current = current.replace("S", "SS*", 1)
    else:
        current = current.replace("S", "a", 1)
    
    steps.append(current)

# Print derivation steps
print("Leftmost derivation steps:")
for i, step in enumerate(steps):
    print(f"Step {i}: {step}")
