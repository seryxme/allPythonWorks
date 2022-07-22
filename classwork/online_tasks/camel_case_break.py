def solution(s):
    from string import ascii_uppercase
    last_index = 0
    for letter in s:
        if letter == " ":
            index = s.find(letter)
            s = s[0:index] + '' + s[index+1:]
            continue
        for alpha in ascii_uppercase:
            if letter == alpha:
                index = s.find(letter, (last_index+1))
                s = s[0:index] + ' ' + s[index:]
                last_index = index+1
                break

    return s


print(solution("break  CamelCase"))

