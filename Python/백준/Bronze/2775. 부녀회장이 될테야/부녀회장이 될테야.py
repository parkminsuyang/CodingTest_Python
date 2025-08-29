# 해당 집의 거주민 수 출력
# 아래층 1호 ~ b호 수의 합 만큼 사람들을 데려오 ㅏ살아야 한다.
# k층 n호 몇명?
# 0층 부터, 각 층 1호부터, 0층 i호 i명

t=int(input())


def live(k,n):

    if n==1:
        return 1

    else:
        people = [[0]*(n+1) for _ in range(k+1)]
        people[0][1]=1
        for w in range(2,n+1):
            people[0][w]=people[0][w-1]+1

        for j in range(1,k+1):
            for o in range(1,n+1):
                people[j][o]=people[j-1][o]+people[j][o-1]


        return people[k][n]




for _ in range(t):
    k = int(input())
    n = int(input())
    print(live(k, n))
