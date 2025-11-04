grammar = {
    "E": [["T", "E'"]],
    "E'": [["+", "T", "E'"], ["ε"]],
    "T": [["F", "T'"]],
    "T'": [["*", "F", "T'"], ["ε"]],
    "F": [["(", "E", ")"], ["id"]]
}

FIRST = {A: set() for A in grammar}
FOLLOW = {A: set() for A in grammar}
FOLLOW["E"].add("$")  # start symbol

def FIRST_of(X):
    if X not in grammar:      # terminal
        return {X}
    for prod in grammar[X]:
        for s in prod:
            f = FIRST_of(s)
            FIRST[X] |= (f - {"ε"})
            if "ε" not in f: break
        else:
            FIRST[X].add("ε")
    return FIRST[X]

def calc_FOLLOW():
    changed = True
    while changed:
        changed = False
        for A, prods in grammar.items():
            for prod in prods:
                for i, B in enumerate(prod):
                    if B in grammar:   # B is non-terminal
                        before = set(FOLLOW[B])
                        beta = prod[i+1:]
                        if beta:
                            fb = set()
                            for x in beta:
                                f = FIRST_of(x)
                                fb |= (f - {"ε"})
                                if "ε" not in f: break
                            else:
                                FOLLOW[B] |= FOLLOW[A]
                            FOLLOW[B] |= fb
                        else:
                            FOLLOW[B] |= FOLLOW[A]
                        if before != FOLLOW[B]:
                            changed = True

for A in grammar: FIRST_of(A)
calc_FOLLOW()

print("FIRST:", FIRST)
print("FOLLOW:", FOLLOW)
