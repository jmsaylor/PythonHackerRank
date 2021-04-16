def rotate(arr, n):
    n = n % len(arr)
    return arr[n:] + arr[:n]


arr = rotate([1, 2, 3], 5)
print(arr)
