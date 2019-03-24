def compareTriplets(a, b):
    aliceScore = sum([1 if aval > bval else 0 for aval, bval in zip(a, b)])
    bobScore = sum([1 if aval < bval else 0 for aval, bval in zip(a, b)])
    return [aliceScore, bobScore]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(" ".join(map(str, result)))
