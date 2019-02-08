N = int(input())
myList = []
for i in range(N):
    line = input().split()
    command = line[0]
    arg = line[1:]
    if command != "print":
        eval("myList." + command + "(" + ",".join(arg) + ")")
    else:
        print(myList)
