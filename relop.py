# Simple Token class
class Token:
    def __init__(self, token_type, attribute=None):
        self.token_type = token_type
        self.attribute = attribute

    def __repr__(self):
        return f"TOKEN(type={self.token_type}, attribute={self.attribute})"

# Super simple getRelop function
def getRelop(input_string):
    t = Token("RELOP")

    if input_string == "<":
        t.attribute = "LT"
    elif input_string == "<=":
        t.attribute = "LE"
    elif input_string == "<>":
        t.attribute = "NE"
    elif input_string == "=":
        t.attribute = "EQ"
    elif input_string == ">":
        t.attribute = "GT"
    elif input_string == ">=":
        t.attribute = "GE"
    else:
        raise ValueError(f"'{input_string}' is not a valid relop")

    return t

# Test cases
tests = ["<", "<=", "<>", "=", ">", ">="]

for t in tests:
    print(f"Input: '{t}'")
    token = getRelop(t)
    print("Output:", token)
