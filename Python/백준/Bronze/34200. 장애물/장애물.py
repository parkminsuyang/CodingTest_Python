import sys
input=sys.stdin.readline

n=int(input())
obstacle=list(map(int,input().split()))

cur=0
cnt=0
for o in obstacle:
    if cur==o:
        print(-1)
        sys.exit()

    if (o-cur-1)%2==1:
        cnt+=((o-cur-1)//2+1)
    else:
        cnt += ((o - cur-1) // 2)
    cnt+=1
    cur=o+1
print(cnt)