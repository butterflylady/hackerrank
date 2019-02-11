def swap_case(s):
    s_modif = ""
    for char in s:
        s_modif += char.swapcase()
    return s_modif


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
