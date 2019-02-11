def print_formatted(number):
    for i in range(1, n + 1):
        width = len(bin(n)) - 2
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
