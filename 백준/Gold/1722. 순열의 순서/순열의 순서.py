import sys
input=sys.stdin.readline

n=int(input()) #1~n 으로 구성된 순열들
num=list(map(int,input().split())) #1+k번째 or 2+순열(몇번째인지?)

fact=[1]*(n+1)

for i in range(1,n+1):
    fact[i]=fact[i-1]*i


if num[0]==1:
    k=num[-1]
    res=[]
    k-=1
    nums=[i for i in range(1,n+1)]

    for i in range(n-1,-1,-1):
        idx=k//fact[i]
        k%=fact[i]
        res.append(nums[idx])
        nums.pop(idx)
    print(*res)

else:
    num=num[1:] #실제 순열
    nums = [i for i in range(1, n + 1)] #남은 숫자
    res=1 #순서
    for i in range(n):
        idx=nums.index(num[i]) #현재 순열 자리 숫자가 남은 숫자 리스트에서 몇번째인지
        res+=idx*fact[n-1-i] #현재 자리 앞에 나올 수 있는 수 더하기
        nums.pop(idx) #사용 수 제거
    print(res)
