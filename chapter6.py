import re

# Easy Three Address Code (TAC) maker

expr = input("Enter expression: ") or "a + a*(b-c) + (b-c)*d"

# Step 1: make postfix
def postfix(e):
    p = {'+':1, '-':1, '*':2, '/':2}
    out, st = [], []
    # ✅ use re.findall so no need for spaces
    for t in re.findall(r'\w+|[()+\-*/]', e):
        if t.isalnum():
            out.append(t)
        elif t in p:
            while st and st[-1] in p and p[st[-1]] >= p[t]:
                out.append(st.pop())
            st.append(t)
        elif t == '(':
            st.append(t)
        elif t == ')':
            while st and st[-1] != '(':
                out.append(st.pop())
            st.pop()
    while st:
        out.append(st.pop())
    return out

# Step 2: make 3-address code
def make_code(post):
    st = []
    n = 1
    for t in post:
        if t.isalnum():
            st.append(t)
        else:
            if len(st) < 2:
                print("Invalid expression!")
                return
            b = st.pop()
            a = st.pop()
            temp = f"t{n}"
            print(f"{temp} = {a} {t} {b}")
            st.append(temp)
            n += 1
    if st:
        print("Result =", st[0])
    else:
        print("No result (check your input).")

# Run
post = postfix(expr)
make_code(post)
