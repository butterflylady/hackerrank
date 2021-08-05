def getWays(amount, coins):
    # amount: integer, the amount to make change for
    # ar: an array of integers, the available coin denominations
    # The function is expected to return an integer number of ways to make change
    coins=sorted(coins)
    num_ways = [[0]*(amount+1) for i in range(len(coins))]
    for i in range(len(coins)):
        num_ways[i][0]=1

    for j in range(1,amount+1):
        if j%coins[0]==0:
            num_ways[0][j]=1
        else:
            num_ways[0][j]=0

    for i in range(1,len(coins)):
        for j in range(1,amount+1):
            if coins[i]>j:
                num_ways[i][j]=num_ways[i-1][j]
            else:
                num_ways[i][j]=num_ways[i-1][j]+num_ways[i][j-coins[i]]
    return int(num_ways[len(coins)-1][amount])


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))
    ways = getWays(n, c)

    print(ways)
