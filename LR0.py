from collections import defaultdict

# Grammar input
grammar = {
    "E'": ["E"],
    "E": ["E+T", "T"],
    "T": ["T*F", "F"],
    "F": ["(E)", "i"]
}

# Function to add dot at beginning
def add_dot(prod):
    return "." + prod

# Closure function
def closure(items):
    closure_set = set(items)

    while True:
        new_items = set(closure_set)

        for item in closure_set:
            if "." in item:
                dot_pos = item.index(".")
                if dot_pos < len(item) - 1:
                    symbol = item[dot_pos + 1]

                    if symbol in grammar:
                        for prod in grammar[symbol]:
                            new_items.add(symbol + "->" + add_dot(prod))

        if new_items == closure_set:
            break

        closure_set = new_items

    return closure_set


# GOTO function
def goto(items, symbol):
    moved = set()

    for item in items:
        if "." in item:
            dot_pos = item.index(".")
            if dot_pos < len(item) - 1 and item[dot_pos + 1] == symbol:
                new_item = item[:dot_pos] + symbol + "." + item[dot_pos + 2:]
                moved.add(new_item)

    return closure(moved)


# Get all symbols
def get_symbols():
    symbols = set()
    for head in grammar:
        for prod in grammar[head]:
            for ch in prod:
                symbols.add(ch)
    return symbols


# Canonical Collection
def canonical_collection():
    start_item = {"E'->.E"}
    C = [closure(start_item)]

    symbols = get_symbols()

    while True:
        new_states = []

        for state in C:
            for sym in symbols:
                g = goto(state, sym)
                if g and g not in C and g not in new_states:
                    new_states.append(g)

        if not new_states:
            break

        C.extend(new_states)

    return C


# -------- MAIN --------
states = canonical_collection()

for i, state in enumerate(states):
    print(f"\nI{i}:")
    for item in state:
        print(item)
