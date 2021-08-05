def maxSubarray(arr):
    # arr: an array of integers
    # The function is expected to return an array of two integer

    sorted_array = sorted(arr.copy(), reverse=True)
    max_sum_subseq = sorted_array[0]
    for i in range(1, len(sorted_array)):
        if sorted_array[i] >= 0:
            max_sum_subseq += sorted_array[i]
        else:
            break

    sums = [0] * len(arr)
    sums[0] = arr[0]
    for j in range(1, len(arr)):
        sums[j] = max(arr[j], sums[j - 1] + arr[j])

    max_sum_contiguous_subseq = max(sums)

    return max_sum_contiguous_subseq, max_sum_subseq


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = maxSubarray(arr)
        print(result)
