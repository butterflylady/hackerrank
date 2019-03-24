def plusMinus(arr):
    n = len(arr)
    positiveFr = print(round(len([x for x in arr if x > 0]) / n, 6))
    negativeFr = print(round(len([x for x in arr if x < 0]) / n, 6))
    zeroFr = print(round(len([x for x in arr if x == 0]) / n, 6))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
