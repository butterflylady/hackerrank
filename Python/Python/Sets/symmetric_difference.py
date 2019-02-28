m = int(input())
mlst = set(list(map(int, input().split())))

n = int(input())
nlst = set(list(map(int, input().split())))

lst_union = mlst.union(nlst)
lst_intersection = mlst.intersection(nlst)
sym_dif = lst_union.difference(lst_intersection)
for item in sorted(sym_dif):
    print(item)
