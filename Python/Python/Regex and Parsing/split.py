import re

regex_pattern = r"[,.]"
print(*re.split(regex_pattern, input()), sep="\n")
