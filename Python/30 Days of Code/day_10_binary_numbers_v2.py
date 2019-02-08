if __name__ == '__main__':
    n = int(input())
    numbers = bin(n)[2:].split('0')
    length = [len(num) for num in numbers]
    print(max(length))
