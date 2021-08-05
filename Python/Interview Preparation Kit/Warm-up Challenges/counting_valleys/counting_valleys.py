## https://www.hackerrank.com/challenges/counting-valleys/problem
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

def counting_valleys(steps, path):
    current_level = 0
    num_valley = 0
    try:
        if steps in range(2, 10 ^ 6 + 1):
            if set(path).issubset(("U", "D")):
                for step in path:
                    if step == "U":
                        current_level += 1
                        if current_level==0:
                            num_valley += 1
                    else:
                        current_level -= 1
            else:
                raise ValueError("Constraints: path[i] in {'U','D'}")
        else:
            raise ValueError ("Constraints: 2<=steps<=10^6")
    except ValueError as ve:
        print(ve)
    return num_valley


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = counting_valleys(steps, path)
    print(result)
