n = int(input())
arr = map(int, input().split())
sortedSet = sorted(set(arr), reverse=True)
print(sortedSet[1])
