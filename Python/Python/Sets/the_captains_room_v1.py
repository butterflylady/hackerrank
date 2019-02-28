from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
a = Counter(arr)
print([num for num, val in a.items() if val != n][0])
