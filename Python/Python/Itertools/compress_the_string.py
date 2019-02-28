from itertools import groupby

s = input()  # ex. s=1222311 or s="AAAABBBCCDAA"
print(*[(len(list(g)), int(k)) for k, g in groupby(s)])
