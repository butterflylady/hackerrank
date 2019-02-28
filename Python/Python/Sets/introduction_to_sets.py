def average(array):
    myset = set(array)
    average_height = sum(myset) / len(myset)
    return average_height


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
