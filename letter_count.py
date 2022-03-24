def letter_count(user_in):
    diction = {}
    for i in user_in:
        if not i in diction:
            diction[i] = 1
        else:
            diction[i] += 1
    return diction

print(letter_count(input()))
