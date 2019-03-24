from collections import Counter


def migratoryBirds(arr):
    value_count = Counter(sorted(arr))
    return value_count.most_common(3)[0][0]


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(str(result) + '\n')
