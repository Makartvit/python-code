wrd = string.split()
    for i in range(len(wrd)):
        if len(wrd[i]) > 6:
            wrd[i] = wrd[i][:6] + '*'
    return ' '.join(wrd)

for word in wrd:
        print(word)


values = 0
    for string in words:
        if len(string) >= 2 and string[0] == string[-1]:
            values += 1
    return values


wrd = string.split()
    for word in wrd:
        if len(word) > 6:
            word = word[:6] + '*'
        print(word)