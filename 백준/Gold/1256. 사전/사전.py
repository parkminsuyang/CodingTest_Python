import sys
import math

input=sys.stdin.readline

#n개의 'a', m개의 'z'와 알파벳순
#k 번째 문자열 출력 ->없으면 -1
n,m,k=map(int,input().split())
total=n+m
if math.comb(n+m,n)<k:
    print(-1)
else:
    res=[]
    while n+m>0:
        if n==0:
            res.append('z')
            m-=1
        elif m==0:
            res.append('a')
            n-=1

        else:
            cnt=math.comb(n+m-1,n-1) #지금 a하면 몇개?
            if k<=cnt:
                res.append('a')
                n-=1
            else:
                res.append('z')
                m-=1
                k-=cnt


    print(''.join(res))