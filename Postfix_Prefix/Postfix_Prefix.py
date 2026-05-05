# Function to define precedence
def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0


# INFIX → POSTFIX
def infix_to_postfix(expression):
    stack = []
    output = []

    tokens = list(expression.replace(" ", ""))

    for ch in tokens:
        if ch.isalnum():  # operand
            output.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('

        else:  # operator
            while (stack and precedence(stack[-1]) >= precedence(ch)):
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


# INFIX → PREFIX
def infix_to_prefix(expression):
    # Reverse expression
    expression = expression[::-1]

    # Swap brackets
    expression = list(expression)
    for i in range(len(expression)):
        if expression[i] == '(':
            expression[i] = ')'
        elif expression[i] == ')':
            expression[i] = '('

    expression = ''.join(expression)

    # Convert to postfix
    postfix = infix_to_postfix(expression)

    # Reverse postfix to get prefix
    prefix = postfix[::-1]

    return prefix


# -------- MAIN --------
expr = input("Enter Infix Expression: ")

postfix = infix_to_postfix(expr)
prefix = infix_to_prefix(expr)

print("\nPostfix Expression:", postfix)
print("Prefix Expression:", prefix)
