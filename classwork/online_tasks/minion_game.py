def word_former(string1):
    count = 1
    word_coll = []

    while count <= len(string1):
        x = 0
        y = count
        while y <= len(string1):
            word_coll.append(string1[x:y])
            x = x + 1
            y = y + 1
        count += 1
    return  word_coll


def word_former2(string1):
    count = 1
    i = 1
    word_coll = set()
    word_coll2 = set()

    while i <= len(string1):
        while count <= len(string1):
            x = 0
            y = count
            while y <= len(string1):
                word_coll2.add(string1[x:y])
                x = x + 1
                y = y + 1
            count += 1
        word_coll.update(word_coll2)
        string1 = string1[i:] + string1[:i]
    return word_coll

def unique_words(new_list):
    lst = []
    for word in new_list:
        if word not in lst:
            lst.append(word)

    return lst


def minion_game(new_string):
    new_list = word_former(new_string.upper())
    lst = unique_words(new_list)

    stuart_score = 0
    kevin_score = 0

    for word in lst:
        if word[0] in "AEIOU":
            kevin_score += new_list.count(word)
        elif word[0] not in "AEIOU":
            stuart_score += new_list.count(word)

    # if stuart_score > kevin_score:
    #     return print(f"Stuart {stuart_score}")
    # elif stuart_score < kevin_score:
    #     return print(f"Kevin {kevin_score}")
    # else:
    #     return print("Draw!")
    return print(new_list)


# minion_game("supercalifragilisticespialidocious")
# minion_game("charming")
# minion_game("neverland")
# minion_game("auspicious")
# minion_game("monkey")

print(word_former2("monkey"))