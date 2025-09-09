import sys

input=sys.stdin.readline
n=int(input())
num=n
nums=[[] for _ in range(11)]
cnt=0

for i in range(2,11):

    while n>0:
        s=0
        nums[i].append(n%i)
        n=n//i
        s+=1
    else:
        n=num

        if nums[i]==(nums[i][::-1]):
            cnt+=1
            print(i,end=" ")
            for j in range(len(nums[i])):
                print(nums[i][j],end="")
            print()

if not cnt:
    print("NIE")