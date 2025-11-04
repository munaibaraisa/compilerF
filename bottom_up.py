tokens = ["id", "*", "id"]
stack = []

def bottom_up_parse(tokens):
    stack = []
    for t in tokens:
        stack.append(t)
        print(f"Shift: {stack}")

        # Reduce F -> id
        while "id" in stack:
            index = stack.index("id")
            stack[index] = "F"
            print(f"Reduce: F -> id, Stack: {stack}")

        # Reduce T -> T * F
        while len(stack) >= 3 and stack[-3:] == ["T", "*", "F"]:
            stack[-3:] = ["T"]
            print(f"Reduce: T -> T * F, Stack: {stack}")

        # Reduce T -> F
        while "F" in stack:
            index = stack.index("F")
            stack[index] = "T"
            print(f"Reduce: T -> F, Stack: {stack}")

    # Final check: Reduce E -> T
    if stack == ["T"]:
        print("Parsing successful! Bottom-Up Parse Tree complete.")
    else:
        print("Parsing failed.")

bottom_up_parse(tokens)
