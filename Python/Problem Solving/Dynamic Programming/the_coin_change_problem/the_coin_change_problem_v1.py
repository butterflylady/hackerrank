def getWays(amount, coins):
    # amount: integer, the amount to make change for
    # ar: an array of integers, the available coin denominations
    # The function is expected to return an integer number of ways to make change
    coins=sorted(coins)
    num_ways = [0]*(amount+1)
    num_ways[0]=1

    for coin in coins:
        for j in range(coin,amount+1):
            num_ways[j]+=num_ways[j-coin]
    return num_ways[amount]


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))
    ways = getWays(n, c)

    print(ways)
