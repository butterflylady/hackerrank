n = int(input())
for i in range(n):
    str_ev = ""
    str_odd = ""
    text = input()
    for j in range(0, len(text)):
        if (j + 1) % 2 == 0:
            str_ev += text[j]
        else:
            str_odd += text[j]
    print(str_odd, str_ev)
