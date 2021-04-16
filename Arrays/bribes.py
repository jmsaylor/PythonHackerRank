import sys

def minimumBribes(q):
    is_chaotic = False
    for i, Pos in enumerate(q, start=1):
        if Pos - i > 2:
            is_chaotic = True

    bribes = 0

    for z in range(3):
        print(z)
        for i in range(len(q) - 1):
            if q[i] > i + 1:
                q[i], q[i + 1] = q[i + 1], q[i]
                print(q)
                bribes += 1

    print(bribes if is_chaotic == False else "Too chaotic")


minimumBribes([1, 2, 5, 3, 4, 7, 8, 6])

