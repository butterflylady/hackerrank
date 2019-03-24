from collections import Counter

s = input()
most_common = Counter(sorted(s)).most_common(3)
for letter_num in most_common:
    print(letter_num[0], letter_num[1])
