import sys
input=sys.stdin.readline

n=int(input())
wait=[]
max_cnt=0
max_wait=0

for _ in range(n):
    nums=list(map(int,input().split()))
    if nums[0]==1:
        wait.append(nums[1])
        if len(wait)>max_cnt:
            max_cnt=len(wait)
            max_wait=wait[-1]
        elif len(wait)==max_cnt:
            if max_wait>wait[-1]:
                max_wait=wait[-1]
    else:
        wait.pop(0)
print(max_cnt, max_wait)