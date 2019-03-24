import re

'''
A valid mobile number is a ten digit number starting with a 7, 8 or 9.
'''

n = int(input())

for i in range(n):
    phone = input()
    pattern = '^(7|8|9)\d{9}$'  # a ten digit number starting with a 7, 8  or 9.
    print("YES" if re.match(pattern, phone) else "NO")
