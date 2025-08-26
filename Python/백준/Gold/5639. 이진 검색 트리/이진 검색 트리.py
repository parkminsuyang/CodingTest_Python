import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.read

nums=list(map(int,input().split()))

def posttoback(start,end):

    if start>end:

        return

    root=nums[start]

    #좌/우 분기 찾기

    idx=start+1

    for i in range(idx,end+1):

        if nums[i]>root:

            posttoback(idx,i-1)

            posttoback(i, end)

            break

    else:

        posttoback(idx,end)

    print(root)

posttoback(0,len(nums)-1)