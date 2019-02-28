m = int(input())
setA = set(map(int, input().split()))
n = int(input())
while n > 0:
    command, num = input().split()
    set_update = set(map(int, input().split()))
    eval("setA.{0}({1})".format(command, set_update))  # or eval("setA."+command+"("+"set_update"+")")
    n -= 1
print(sum(setA))
