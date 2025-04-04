#정렬스딱스를찵여오걸아
import sys
n=int(sys.stdin.readline().strip())
num=list(map(int,sys.stdin.readline().strip().split()))


for i in range(n-1):
    for j in range(i+1,n):
        if num[j]<num[i]:
            num[j],num[i]=num[i],num[j]

partSum = [0]*(n)
partSum[0]=num[0]

for k in range(1,n):
    partSum[k]=partSum[k-1]+num[k]
print(sum(partSum))