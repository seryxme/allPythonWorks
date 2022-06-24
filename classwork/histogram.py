def letter_counter(statement):
    import string
    alphabets = string.ascii_lowercase

    dicto = {}
    count = []
    for letter in alphabets:
        if letter in statement:
            count.append(statement.lower().count(letter))
        else:
            count.append(0)

    for letter in range(len(alphabets)):
        dicto[alphabets[letter]] = count[letter]

    return dicto


dict2 = letter_counter("Alabama is not a big town")

print(dict2)


def letter_counter2(statement):
    import string
    alphabets = string.ascii_lowercase

    dicto = {}
    for letter in alphabets:
        dicto[letter] = (statement.lower().count(letter))

    return dicto


dict3 = letter_counter2("Colorado is the biggest of all United States territories")

print(dict3)


def letter_counter3(statement):
    import string; return {letter: statement.lower().count(letter) for letter in string.ascii_lowercase}


print(letter_counter3("Colorado is the biggest of all United States territories"))


def letter_counter4(statement):
    lst = []
    #return len(set(statement))
    return len([lst.append(letter) for letter in statement.lower() if letter not in lst and letter != " "])



print(letter_counter4("Alabama"))

print(letter_counter4("Foo Fighters"))

print(letter_counter4("SemiDemiLastCard"))