def count_substring(string, sub_string):
    ind = 0
    count = 0
    while ind < len(string):
        ind = string.find(sub_string, ind)
        if ind >= 0:
            ind += 1
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
