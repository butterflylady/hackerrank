import re

'''
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(0)) # The entire match
print(m.group(1))       # The first parenthesized subgroup.
print(m.group(2))       # The second parenthesized subgroup.
print(m.group(3))       # The third parenthesized subgroup.
print(m.group(1,2,3))   # Multiple arguments give us a tuple.

print(m.groups())       # A tuple containing all the subgroups of the match.

ma = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(ma.groupdict())

'''
s = input()
reg = r'([a-zA-Z\d])\1+'  # \1+  Occurrence of an alphanumeric character in s that has consecutive repetitions.
m = re.search(reg, s.strip())
print(m.group(1) if m else -1)
