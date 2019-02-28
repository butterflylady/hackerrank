from itertools import combinations

s, k = input().split()
s_list = sorted(list(s))

for i in range(1, int(k) + 1):
    comb_list = list(combinations(s_list, i))
    for item in comb_list:
        print(("".join(item)))
