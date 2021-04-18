def isValid(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    flag = False
    val = min(count.values())

    print(val)

    for _, v in count.items():
        if v == val:
            continue
        elif v == val + 1:
            if flag:
                return "NO"
            flag = True
        elif v > val + 1:
            return "NO"

    return "YES"

isValid('aabbcd')