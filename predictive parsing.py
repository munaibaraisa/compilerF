# Simple Recursive Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.look = tokens[0] if tokens else None

    def match(self, t):
        if self.look == t:
            print("Matched:", t)
            self.pos += 1
            self.look = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        else:
            raise SyntaxError(f"Expected {t}, found {self.look}")

    def stmt(self):
        if self.look == "if":
            print("stmt → if ( expr ) stmt")
            self.match("if"); self.match("("); self.expr(); self.match(")"); self.stmt()
        elif self.look == "for":
            print("stmt → for ( optexpr ; optexpr ) stmt")
            self.match("for"); self.match("("); self.optexpr(); self.match(";"); self.optexpr(); self.match(")"); self.stmt()
        elif self.look == "other":
            print("stmt → other"); self.match("other")
        elif self.look == "EXPR":
            print("stmt → expr ;"); self.expr(); self.match(";")
        else:
            raise SyntaxError(f"Unexpected token {self.look}")

    def optexpr(self):
        if self.look == "EXPR":
            print("optexpr → expr"); self.expr()
        elif self.look in [";",")"]:
            print("optexpr → ε")  # do nothing

    def expr(self):
        if self.look == "EXPR":
            print("expr → EXPR"); self.match("EXPR")
        else:
            raise SyntaxError(f"Expected EXPR, found {self.look}")


# ---------------- Examples ----------------
examples = [
    ["EXPR",";"],                 # expr ;
    ["if","(","EXPR",")","other"], # if statement
    ["for","(","EXPR",";",")","other"] # for statement
]

for i,toks in enumerate(examples,1):
    print(f"\n=== Example {i} === Input:", " ".join(toks))
    parser = Parser(toks)
    try:
        parser.stmt()
        print("Parsing successful ✅" if parser.look is None else "Extra tokens left:", parser.look)
    except SyntaxError as e:
        print("Syntax Error:", e)
