from collections import Counter

n = int(input())

count = Counter([input() for _ in range(n)])
print(len(count.keys()))
print(*list(count.values()))
