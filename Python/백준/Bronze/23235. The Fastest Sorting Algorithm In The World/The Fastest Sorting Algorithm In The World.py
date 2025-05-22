import sys

input=sys.stdin.readline
i=1
while True:
    num=list(map(int,input().split()))
    if num==[0]:
        exit()
    print(f'Case {i}: Sorting... done!')
    i+=1
