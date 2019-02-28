n, m = map(int, input().split())
arr = list(map(int, input().split()))
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))
happiness = 0
for item in arr:
    if item in like:
        happiness += 1
    elif item in dislike:
        happiness -= 1
    else:
        pass
print(happiness)
