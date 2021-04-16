def minimumBribes(q):
    bribes = 0
    is_chaotic = False
    for original, current in enumerate(q, start=1):
        print("current", current, "original", original)
        if current < original:
            continue
        if current - original > 2:
            is_chaotic = True
            break

        bribes += current - original

    result = bribes if is_chaotic == False else "Too Chaotic"

    print(result)


arr = minimumBribes([2, 1, 5, 3, 4])
print(arr)
