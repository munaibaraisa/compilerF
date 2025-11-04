from tabulate import tabulate

# ACTION and GOTO tables
ACTION = {
    0: {"id": ("S",5), "(":("S",4)}, 1:{"+":("S",6), "$":("ACC",)},
    2:{"+":("R",2),"*":("S",7),")":("R",2),"$":("R",2)}, 3:{"+":("R",4),"*":("R",4),")":("R",4),"$":("R",4)},
    4:{"id":("S",5),"(":("S",4)},5:{"+":("R",6),"*":("R",6),")":("R",6),"$":("R",6)},
    6:{"id":("S",5),"(":("S",4)},7:{"id":("S",5),"(":("S",4)},8:{"+":("S",6),")":("S",11)},
    9:{"+":("R",1),"*":("S",7),")":("R",1),"$":("R",1)},10:{"+":("R",3),"*":("R",3),")":("R",3),"$":("R",3)},
    11:{"+":("R",5),"*":("R",5),")":("R",5),"$":("R",5)}
}
GOTO = {0:{"E":1,"T":2,"F":3},4:{"E":8,"T":2,"F":3},6:{"T":9,"F":3},7:{"F":10}}

# Grammar productions
productions = {
    1: ("E", ["E","+","T"]),2:("E",["T"]),3:("T",["T","*","F"]),4:("T",["F"]),
    5:("F",["(","E",")"]),6:("F",["id"])
}

# Show grammar
def show_grammar():
    print("\nGrammar:")
    print(tabulate([[i,f"{lhs} → {' '.join(rhs)}"] for i,(lhs,rhs) in productions.items()],
                   headers=["No.","Production"], tablefmt="fancy_grid"))

# LR parse
def lr_parse(tokens):
    stack = [0]; tokens.append("$"); index=0; step=1; rows=[]
    while True:
        state = stack[-1]; tok = tokens[index]
        action = ACTION.get(state, {}).get(tok)
        if not action: rows.append([step, stack[:], tokens[index:], f"Error ❌ at {tok}"]); break
        if action[0]=="S":
            stack += [tok, action[1]]; rows.append([step, stack[:], tokens[index:], f"Shift {tok}, goto {action[1]}"]); index+=1
        elif action[0]=="R":
            num=action[1]; lhs,rhs=productions[num]; pop_len=2*len(rhs)
            if pop_len>0: stack=stack[:-pop_len]
            state=stack[-1]; stack += [lhs, GOTO[state][lhs]]
            rows.append([step, stack[:], tokens[index:], f"Reduce by {lhs} → {' '.join(rhs)}"])
        elif action[0]=="ACC":
            rows.append([step, stack[:], tokens[index:], "Accept ✅"]); break
        step+=1
    print(tabulate([[i+1]+row for i,row in enumerate(rows)],
                   headers=["Step","Stack","Input","Action"], tablefmt="fancy_grid"))

# ---------------- Example ----------------
show_grammar()
for i,toks in enumerate([["id","+","id","*","id"], ["(","id","+","id",")","*","id"], ["id","*","+","id"]],1):
    print(f"\n--- Parsing tokens{i} ---")
    lr_parse(toks.copy())
