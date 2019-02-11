def solve(s):
    s_new = ""
    for i in range(len(s)):
        if (i == 0) or (s[i - 1] == " " and s[i] != " "):
            s_new += s[i].capitalize()
        else:
            s_new += s[i]
    return s_new


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
