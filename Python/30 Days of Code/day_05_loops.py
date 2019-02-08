def multiple(n):
    for i in range(1, 11):
        print(str(n), "x", str(i), "=", i * n)


if __name__ == '__main__':
    n = int(input())
    multiple(n)
