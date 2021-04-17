def maxSubsetSum(arr):
    table = [0] * (len(arr) + 3)

    print("length", len(table), table[0], table)
    for i, value in enumerate(arr, start=3):
        if value < 1:
            table[i] = max(table[i - 2], table[i - 3])
        else:
            table[i] = max(table[i - 2] + value, table[i - 3] + value, value)

    length = len(table)
    return max(table[length - 1], table[length - 2])


res = maxSubsetSum([4,2,-4,4,-5,8,7,-1])
print(res)