'''
print(re.findall(r'\w', 'http://www.hackerrank.com/'))
re.finditer(r'\w', 'http://www.hackerrank.com/')
print(list(map(lambda x: x.group(), re.finditer(r'\w', 'http://www.hackerrank.com/'))))
'''
import re

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
match = re.findall("(?<=[%s])([%s]{2,})[%s]" %(CONSONANTS, VOWELS,CONSONANTS), input(), flags=re.I)
print('\n'.join(match or ['-1']))
