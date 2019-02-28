t = int(input())
for i in range(t):
    num_a = int(input())
    set_a = set(map(int, input().split()))
    num_b = int(input())
    set_b = list(map(int, input().split()))
    print(set_a.issubset(set_b))
