import re

'''
- Number can start with +, - or . symbol (For example:✔+4.50 ✔-1.0 ✔.5 ✔-.7 ✔+.4 ✖-+4.5)
- Number must contain at least  decimal value (For example:✖12. ✔12.0  
- Number must have exactly one . symbol
- Number must not give any exceptions when converted using float(N)
'''

t=int(input())
reg = r'^[+-]?\d*\.\d+$'
'''
    + - 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
    * - 0 or more occurrences of the pattern to its left
    ? - match 0 or 1 occurrences of the pattern to its left 
'''
for _ in range(t):
    print(bool(re.search(reg, input())))
