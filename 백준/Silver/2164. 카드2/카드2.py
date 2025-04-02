from collections import deque
n=int(input())
num=deque(range(1,n+1))
while len(num)>1:
    num.popleft()
    num.append(num.popleft())
print(num[0])
