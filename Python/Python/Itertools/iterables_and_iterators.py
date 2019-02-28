from itertools import combinations

n = int(input())
lst = input().split()
k = int(input())
comb_list = list(combinations(lst, k))
count=0
for item in comb_list:
    if "a" in item:
        count+=1
print(round(count/len(comb_list),4))