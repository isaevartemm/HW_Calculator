def is_float(element: any) -> bool:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def to_rpn(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    output = []
    operators = []
    tokens = expression.split()
    for token in tokens:
        if is_float(token):
            output.append(token)
        elif token in precedence:
            while operators and precedence[token] <= precedence[operators[-1]]:
                output.append(operators.pop())
            operators.append(token)

    while operators:
        if operators[-1] == "(":
            raise ValueError("Mismatched parentheses")
        output.append(operators.pop())
    return " ".join(output)


def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if is_float(token):
            stack.append(float(token))
        elif token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif token == "/":
            b = stack.pop()
            a = stack.pop()
            if b == 0:
                return 'Zero division!'
            stack.append(float(a / b))
        else:
            raise ValueError("Invalid RPN expression")
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    return stack[0]


def f(expression):
    return evaluate_rpn(to_rpn(expression))
