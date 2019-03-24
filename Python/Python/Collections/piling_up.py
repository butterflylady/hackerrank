from collections import deque

t = int(input())

for i in range(t):
    n = int(input())
    mydeque = deque(map(int, input().split()))
    newdeque = deque()
    if mydeque[0] >= mydeque[-1]:
        newdeque.append(mydeque.popleft())
    else:
        newdeque.append(mydeque.pop())

    ans = "Yes"
    while mydeque:
        if mydeque[0] >= mydeque[-1] and mydeque[0] <= newdeque[-1]:
            newdeque.append(mydeque.popleft())
        elif mydeque[0] < mydeque[-1] and mydeque[-1] <= newdeque[-1]:
            newdeque.append(mydeque.pop())
        else:
            ans = "No"
            break
    print(ans)
