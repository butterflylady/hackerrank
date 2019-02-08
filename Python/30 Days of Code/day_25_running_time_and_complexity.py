import math


def primeNumber(n):
    if n == 1:
        ans = "Not prime"
        return ans
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                ans = "Not prime"
                return ans
    ans = "Prime"
    return ans


numCases = int(input())
for i in range(numCases):
    print(primeNumber(int(input())))
