def diagonalDifference(arr):
    n = len(arr)
    diag1 = sum([arr[i][i] for i in range(n)])
    diag2 = sum([arr[i][n - 1 - i] for i in range(n)])
    return abs(diag1 - diag2)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(str(result) + '\n')
