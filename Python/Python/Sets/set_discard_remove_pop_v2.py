n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split() + ['']))
    # If we have a=[1,2,3] then function(*a) is equal to function(1,2,3), "" for pop()
print(sum(s))
