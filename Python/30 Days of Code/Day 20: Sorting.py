def bubleSort(a):
    numSwaps = 0
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwaps += 1
    return a[0], a[-1], numSwaps


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
bubleS = bubleSort(a)
print("Array is sorted in", bubleS[2], "swaps.")
print("First Element:", bubleS[0])
print("Last Element:", bubleS[1])
