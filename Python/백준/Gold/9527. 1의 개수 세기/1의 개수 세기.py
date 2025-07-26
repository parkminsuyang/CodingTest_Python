import sys

input=sys.stdin.readline


a,b=map(int,input().split())


def bi(x):
    cnt=0
    total = 0
    for i in range(55):
        rep=1<<(i+1)
        total+=(x+1)//rep*(1<<i)
        remain=(x+1)%rep
        total+=max(0,remain-(1<<i))
    return total

print(bi(b)-bi(a-1))