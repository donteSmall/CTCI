def revered(string_1):
    #Hunter
#go through string <--
    i = -1
    while i > -len(string_1):
        result.append(string_1[i])
        i -= 1

    for i in range(0, len(string_1)):
        result.append(string_1[-1 - i])

    # Hunter
    # ^    ^
    # i = 0
    # front = H
    # back = r
    # runteH

    # go through the string from back to front

    # pick the frontmost and backmost item and swap them
    # then move inward picking the next frontmost and next backmost
    for i in range(0, length(string_1) / 2):
        back = string_1[-1 - i]
        front = string_1[i]
        string_1[i] = back
        string_1[-1 - i] = front

    return result

#append last item to container <--
#once is done return string
    return string_1[::-1]

#f(abaaaaa) -> ab not ba

def removes_dup(input):
    #inter from front to back of string
    seen = set()
    result=''
    for letter in string:
        if not(letter in seen):
            result +=letter
            seen.add(letter)
    return result
    #if char not in containter, add char
    #else dont add
