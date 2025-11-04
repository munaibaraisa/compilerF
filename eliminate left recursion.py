# Step 1: ব্যবহারকারীর থেকে গ্রামার ইনপুট নেওয়া
grammar = {}
n = int(input("Non-terminals এর সংখ্যা দিন: "))
for _ in range(n):
    nt = input("Non-terminal লিখুন: ")
    prods = input(f"{nt} এর productions (| দিয়ে আলাদা করুন): ").split('|')
    grammar[nt] = [p.strip() for p in prods]  # স্পেস ক্লিয়ার করা

# Step 2: Left recursion দূর করার ফাংশন
def remove_left_recursion(g):
    new_g = {}
    for nt in g:
        alpha = []  # left-recursive parts (যেগুলো nt দিয়ে শুরু)
        beta = []   # non-left-recursive parts
        for prod in g[nt]:
            if prod.startswith(nt):
                alpha.append(prod[len(nt):].strip())  # nt বাদ দিয়ে রাখি
            else:
                beta.append(prod)
        if alpha:  # যদি left recursion থাকে
            nt_dash = nt + "'"  # নতুন non-terminal বানাই
            # মূল nt এর জন্য নতুন production বানানো
            new_g[nt] = [b + " " + nt_dash for b in beta]
            # নতুন nt' এর জন্য production
            new_g[nt_dash] = [a + " " + nt_dash for a in alpha] + ["ε"]  # ε = empty
        else:
            new_g[nt] = g[nt]  # left recursion না থাকলে আগের মতো রাখি
    return new_g

# Step 3: Left recursion remove করা
new_grammar = remove_left_recursion(grammar)

# Step 4: নতুন গ্রামার প্রিন্ট করা
print("\nLeft recursion দূর করার পর গ্রামার:")
for nt, prods in new_grammar.items():
    print(f"{nt} -> {' | '.join(prods)}")
