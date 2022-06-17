def bracketCheck(brackets):
    if len(brackets) % 2 != 0:
        return False
    brac_list = list(brackets)
    brace_open = '{'
    brace_close = '}'
    square_open = '['
    square_close = ']'
    par_open = '('
    par_close = ')'
    open_stack = []
    for bracket in brac_list:
        if bracket == brace_open:
            open_stack.append(bracket)
        if bracket == square_open:
            open_stack.append(bracket)
        if bracket == par_open:
            open_stack.append(bracket)

        if bracket == brace_close:
            if open_stack[-1] == brace_open:
                open_stack.pop()
            else:
                return False
        if bracket == square_close:
            if open_stack[-1] == square_open:
                open_stack.pop()
            else:
                return False
        if bracket == par_close:
            if open_stack[-1] == par_open:
                open_stack.pop()
            else:
                return False

    if len(open_stack) == 0:
        return True
    else:
        return False


brackets = "{{()[]}}"
print(bracketCheck(brackets))

brackets2 = "[({))}(]"
print(bracketCheck(brackets2))

brackets3 = "{()[()])({[]}}"
print(bracketCheck(brackets3))

brackets4 = "{({[]()}())[]}"
print(bracketCheck(brackets4))