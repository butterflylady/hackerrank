N, M = map(int, input().split())
line = N // 2
door_q = []
for i in range(1, N // 2 + 1):
    q = "-" * 3 * line + ".|" + "..|" * (i - 1)
    door_q.append(q)
    line -= 1
for matline in range(N // 2):
    print(door_q[matline] + "".join(reversed(door_q[matline][0:-1])))
print("-" * ((M - 7) // 2) + "WELCOME" + "-" * ((M - 7) // 2))
for matline in range(N // 2):
    print(door_q[len(door_q) - 1 - matline] + "".join(reversed(door_q[len(door_q) - 1 - matline][0:-1])))
