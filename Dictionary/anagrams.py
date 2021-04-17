def sherlockAndAnagrams(s):
    result = 0
    for sublength in range(1, len(s)):
        counts = {}
        i = 0
        while i + sublength <= len(s):
            substring = str(sorted(list(s[i:i+sublength])))
            if substring in counts:
                result += counts[substring]
                counts[substring] += 1
            else:
                counts[substring] = 1
            i += 1

    return result


def permutations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


res = sherlockAndAnagrams("mom")
print(res)
# res = factorial(4)
# print(res)