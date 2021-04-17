def twoStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)

    return "YES" if len(set1 & set2) > 0 else "NO"



print(twoStrings("hat", "bag"))