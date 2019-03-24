import re


def change_symb(match):
    symb = match.group(0)
    if symb == "&&":
        return "and"
    elif symb == "||":
        return "or"


n = int(input())

for i in range(n):
    line = input()
    pattern = '(?<= )(&&|\|\|)(?= )'  # Ex.  s="A && && && && && && B"
    print(re.sub(pattern, change_symb, line))
