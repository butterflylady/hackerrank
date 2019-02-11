def merge_the_tools(string, k):
    lst_str=[string[i:i+k] for i in range(0,len(string),k)]
    for item in lst_str:
        print("".join(sorted(set(item), key=item.index)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)