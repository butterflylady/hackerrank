import re

'''
A valid email address meets the following criteria:
- It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
- The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
- The domain and extension contain only English alphabetical characters.
- The extension is 1, 2, or 3 characters in length.
'''

n = int(input())
for _ in range(n):
    name, email = input().split()
    pattern = '^<[a-zA-Z][\w\.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>$'
    if re.match(pattern, email):
        print(name, email)
