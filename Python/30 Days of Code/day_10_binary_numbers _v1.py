if __name__ == '__main__':
    n = int(input())
    bin_n = bin(n)[2:]
    count_ones = 0
    num_ones = []
    for item in bin_n:
        if item == "1":
            count_ones += 1
        else:
            if count_ones != 0:
                num_ones.append(count_ones)
            count_ones = 0
    if count_ones != 0:
        num_ones.append(count_ones)
    print(max(num_ones))
