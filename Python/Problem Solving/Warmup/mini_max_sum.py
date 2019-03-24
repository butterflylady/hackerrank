def miniMaxSum(arr):
    sortedArr = sorted(arr)
    minSum = sum(sortedArr[0:-1])
    maxSum = sum(sortedArr[1:])
    print(minSum, maxSum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
