def migratoryBirds(arr):
    count = [0] * 6
    for t in arr:
        count[t] += 1
    return count.index(max(count))


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(str(result) + '\n')
