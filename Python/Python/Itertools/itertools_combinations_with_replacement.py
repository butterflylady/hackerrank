from itertools import combinations_with_replacement

s, k = input().split()
s_list = sorted(list(s))
comb_list = list(combinations_with_replacement(s_list, int(k)))
for item in comb_list:
    print(("".join(item)))
