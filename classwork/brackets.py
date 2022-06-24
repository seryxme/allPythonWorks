def bracket_check(brackets):
    if len(brackets) % 2 != 0:
        return False

    brace_open = '{'
    brace_close = '}'
    square_open = '['
    square_close = ']'
    par_open = '('
    par_close = ')'
    open_stack = []
    for bracket in brackets:
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


def bracket_check2(bracks):
    if len(bracks) % 2 != 0:
        return False

    open_stack = []

    for bracket in bracks:
        if bracket in "{[(":
            open_stack.append(bracket)
        elif bracket in "})]":
            if bracket == "}" and open_stack[-1] == "{":
                open_stack.pop()
            elif bracket == "[" and open_stack[-1] == "]":
                open_stack.pop()
            elif bracket == "(" and open_stack[-1] == ")":
                open_stack.pop()
            else:
                return False
        else:
            return False
    return True


brackets1 = "{{()[]}}"
print(bracket_check2(brackets1))

brackets2 = "[({))}(]"
print(bracket_check2(brackets2))

brackets3 = "{()[()])({[]}}"
print(bracket_check2(brackets3))

brackets4 = "{({[]()}())[]}"
print(bracket_check2(brackets4))
