if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr_rev = list(reversed(arr))
    for it in arr_rev:
        print(it, end=" ")
