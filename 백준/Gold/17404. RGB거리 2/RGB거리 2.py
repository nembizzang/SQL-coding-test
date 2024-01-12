'''
동일한 문제 조건에서 일렬로 집을 칠하는 RGB거리 1 문제에서
원형으로 된 집을 칠하는 문제이다.
첫번째 집을 칠했을 때의 색상에 따른 경우를 먼저 나누고 RGB거리 1과 동일한 방식으로 진행하자.
'''
input = open(0).readline

def solution():
    n = int(input())
    houses = [list(map(int,input().split())) for _ in range(n)] # 벽칠 비용
    ans = max_ = 1000*n+1 # 전체 다 최대 비용으로 칠했을 경우+1
    for i in range(3): # 첫 집 색 정하기
        dp = [[max_]*3 for _ in range(n)] # i번째 집을 j번째 색으로 칠하는 경우의 누적 최소 벽칠 비용
        dp[0][i] = houses[0][i] # 첫 집 칠하기(나머지 두 집은 max_)
        for j in range(1,n): # 두번째 집부터 칠하기
            dp[j][0] = houses[j][0] + min(dp[j-1][1],dp[j-1][2])
            dp[j][1] = houses[j][1] + min(dp[j-1][0],dp[j-1][2])
            dp[j][2] = houses[j][2] + min(dp[j-1][0],dp[j-1][1])
            # 이 방식으로 진행하면 첫째 집과 두번째 집을 같은 색으로 칠하는 경우의 최소비용이 max_가 되기에
            # 이후 for문을 진행하면서 이런 경우가 최소값을 정하면서 자연스럽게 배제됨
        dp[-1][i] = max_ # 마지막 집과 첫째집이 같은 색을 칠하는 경우를 배제하기 위해 max_값을 넣어줌
        ans = min(ans,min(dp[-1])) # 첫 집 다른 색일 경우의 ans와 비교하여 최소값
    print(ans)
        
if __name__ == '__main__':
    solution()