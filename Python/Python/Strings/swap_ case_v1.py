def swap_case(s):
    s_modif = ""
    for char in s:
        if char.isupper():
            s_modif += char.lower()
        else:
            s_modif += char.upper()
    return s_modif


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
