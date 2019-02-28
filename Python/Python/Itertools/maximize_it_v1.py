from itertools import product

k, m = map(int, input().split())
lst = []
for i in range(k):
    temp = [a**2 for a in list(map(int, input().split()))[1:]]
    lst.append(temp)

prod_list = list(product(*lst))
max_func = 0
for item in prod_list:
    func = sum(item)
    if func%m > max_func:
        max_func = func%m
print(max_func)

