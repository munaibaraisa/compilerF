def type_conversion():
    table = {}

    # User input for a
    a = int(input("Enter value of a (integer): "))
    table['a'] = ('int', a)
    print(f"a = {a} (int)")

    # User input for multiplying value
    b_input = float(input("Enter a float number to multiply with a: "))

    # int → float conversion
    a_float = float(a)
    result = a_float * b_input
    table['b'] = ('float', result)

    print(f"b = {result} (float)")

    print("\nSymbol Table:")
    for var in table:
        print(var, "=", table[var])

type_conversion()
