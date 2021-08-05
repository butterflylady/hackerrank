
def minimumAbsoluteDifference(arr):
    # arr: an array of integers
    # The function is expected to return the minimum absolute difference found, integer
    sorted_arr=sorted(arr)
    min_diff=abs(sorted_arr[-1]-sorted_arr[0])
    for i in range(len(sorted_arr)-1):
        diff=abs(sorted_arr[i+1]-sorted_arr[i])
        if diff<min_diff:
            min_diff=diff
    return min_diff


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)

