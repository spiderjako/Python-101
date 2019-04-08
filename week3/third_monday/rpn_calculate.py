def find_operator(a ,b , chr):
    if chr == '+':
        return a + b
    elif chr == '-':
        return a - b
    elif chr == '*':
        return a * b
    elif chr == '/':
        return a / b

def rpn_calculate(expression):
    split_expression = expression.split(' ')
    i = 2
    summ = 0
    while i < len(split_expression):
        

        i += 1
    return summ