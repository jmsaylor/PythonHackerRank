def alternatingCharacters(s):
    current = ''
    delete_counter = 0

    for c in s:
        if current != c:
            current = c
        else:
            delete_counter += 1

    return delete_counter
