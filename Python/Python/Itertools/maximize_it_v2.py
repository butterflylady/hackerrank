from itertools import product

k, m = map(int, input().split())
lst = list(list(map(int, input().split()))[1:] for _ in range(k))
results = map(lambda x: sum(i ** 2 for i in x) % m, product(*lst))
print(max(results))
