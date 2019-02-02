import re

t=int(input())
reg = r'^[+-]?\d*\.\d+$'
'''
    + - 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
    * - 0 or more occurrences of the pattern to its left
    ? - match 0 or 1 occurrences of the pattern to its left 
'''
for _ in range(t):
    print(bool(re.search(reg, input())))
