import re

'''
► It must start with a 4,5 or 6. 
► It must contain exactly 16 digits. 
► It must only consist of digits (0-9). 
► It may have digits in groups of 4, separated by one hyphen "-". 
► It must NOT use any other separator like ' ' , '_', etc. 
► It must NOT have 4 or more consecutive repeated digits.
'''

n = int(input())
pattern = r'^(?=[456])(?!.*(\d)(-?\1){3})((\d{4}-?){3}\d{4})$'

for _ in range(n):
    card_num = input()
    if re.match(pattern, card_num):
        print("Valid")
    else:
        print("Invalid")
