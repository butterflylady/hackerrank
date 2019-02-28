n = int(input())
s = set(map(int, input().split()))
m = int(input())
while m > 0:
    line = input().split()
    command = line[0]
    num = (line[1] if command != "pop" else "")
    eval("s." + command + "(" + str(num) + ")")
    m -= 1
print(sum(s))
