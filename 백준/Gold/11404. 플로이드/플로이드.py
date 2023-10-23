input = open(0).readline

def solution(n):
    for k in range(1,n+1): # 중간에 1~n까지의 정류장을 들렀다가는 경우
        for i in range(1,n+1): # 출발 정류장
            for j in range(1,n+1): # 도착 정류장
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]) # 현재 i에서 j의 경로 보다 k를 들렀다가는 것이 빠르다면

    for i in range(1,n+1): # 1~n 정류장 확인
        ans = ''
        for j in range(1,n+1):
            cost = dp[i][j]
            ans += str(0) if cost == inf else str(cost)
            ans += ' '
        print(ans[:-1])
    return

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    inf = float('inf')

    dp = [[inf]*(n+1) for _ in range(n+1)] # dp 생성
    for i in range(n+1) : # 출발 도착이 같을 경우는 0
        dp[i][i] = 0

    for _ in range(m):
        sta,end,w = map(int,input().split())
        dp[sta][end] = min(dp[sta][end], w)
    solution(n)