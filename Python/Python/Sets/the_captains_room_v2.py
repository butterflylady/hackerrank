n = int(input())
arr = list(map(int, input().split()))
roomset = set(arr)
caproom = (sum(roomset) * n - sum(arr)) // (n - 1)
print(caproom)
