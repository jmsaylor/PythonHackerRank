import sys

def minimumBribes(q):
    bribes = 0
    is_chaotic = False
    for i, Pos in enumerate(q):
        if Pos - (i + 1) > 2:
            is_chaotic = True


    print(bribes if is_chaotic is not True else "Too chaotic")



minimumBribes([1, 2, 5, 3, 4, 7, 8, 6])

