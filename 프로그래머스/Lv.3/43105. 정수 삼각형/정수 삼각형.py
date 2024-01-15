'''
i행 j열 도달경로의 최대값은 i-1 행의 j-1,j번째까지 도달 경로의 최대값 + i행 j열 값
위 점화식을 가지고 dp 알고리즘으로 문제 해결
'''
def solution(triangle):
    dp = [0]*len(triangle) # dp[i]는 확인하는 행의 각 열까지 도달하는 최대값
    dp[0] = triangle[0][0]
    for i in range(1,len(triangle)):
        tmp_dp = [0]*len(triangle)
        tmp_dp[0] = triangle[i][0] + dp[0] # 맨 앞자리는 한 칸 오른쪽에서만 내려오는 경로뿐이다.
        for j in range(1,len(triangle[i])):
            tmp_dp[j] = triangle[i][j]+max(dp[j-1:j+1]) # 점화식
        dp = tmp_dp # 확인하는 행 경로별 최대값 갱신
    return max(dp)