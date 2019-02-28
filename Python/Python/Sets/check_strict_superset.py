a_set = set(map(int, input().split()))
n = int(input())
for i in range(n):
    sub_set = set(map(int, input().split()))
    if not a_set.issuperset(sub_set):
        print("False")
        break
else:
    print("True")
