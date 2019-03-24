def birthdayCakeCandles(ar):
    maxHeight = max(ar)
    num = 0
    for item in ar:
        if item == maxHeight:
            num += 1
    return num


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    print(str(result) + '\n')
