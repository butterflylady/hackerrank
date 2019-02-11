import string


def print_rangoli(size):
    letters = string.ascii_lowercase
    pattern = []
    m = 2 * size - 1 + 2 * (size - 1)  # number of symbols in a line
    for i in range(size):
        s = letters[i:size]
        pattern.append("-".join(s[::-1] + s[1:]).center(m, "-"))
    print('\n'.join(pattern[::-1]+pattern[1:]).center(m, "-"))


n = int(input())
print_rangoli(n)
