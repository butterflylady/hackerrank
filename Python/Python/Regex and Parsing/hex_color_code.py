import re

n = int(input())
pattern = '(?<!^)(#(?:[\da-f]{3}){1,2})'

for i in range(n):
    line = input()
    matches = re.findall(pattern, line, re.I)
    if matches:
        print(*matches, sep='\n')
