import re

'''
A valid UID must follow the rules below:
- It must contain at least 2 uppercase English alphabet characters.
- It must contain at least 3 digits (0-9).
- It should only contain alphanumeric characters (a-z, A-Z & 0-9).
- No character should repeat.
- There must be exactly 10 characters in a valid UID.
'''

n = int(input())
pattern = r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(.*[0-9]){3,})[A-Za-z0-9]{10}$'

for _ in range(n):
    uid = input()
    if re.match(pattern, uid):
        print("Valid")
    else:
        print("Invalid")
