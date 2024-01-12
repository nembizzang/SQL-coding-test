'''
원형으로 된 집들을 이웃끼리 다른 색으로 칠하는 최소값을 구하는 문제이다.

'''
input = open(0).readline

def solution():
    n = int(input()) # 집의 개수
    houses = [list(map(int,input().split())) for _ in range(n)] # 집마다 벽칠 비용
    max_ = 1000*n+1 # 최대비용*집의 개수+1
    dp = [[max_]*3 for _ in range(n)]
    dp[0] = houses[0] # 첫번째 집을 칠하는 최소 비용은 고정
    nth = 1 # 두번째 집부터 벽칠 시작
    while nth < n : # 탐색 완료 조건
        r,g,b = houses[nth] # 이번 집의 벽칠 비용
        R,G,B = min(dp[nth-1][1:])+r, min(dp[nth-1][::2])+g, min(dp[nth-1][:2])+b # r,g,b 별 최소값
        dp[nth] = [R,G,B]
        nth+=1
    print(min(dp[-1]))

if __name__ == '__main__':
    solution()