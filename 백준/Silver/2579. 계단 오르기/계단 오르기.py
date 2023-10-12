'''
dp[i][j] = i번째 계단에 [한 칸 만 올라온 경우, 두 칸 올라온 경우]
마지막 계단에서 얻을 수 있는 점수 중 최대값을 반환하자
dp[i][0] = 계단을 한 칸 만 올라와서 얻는 점수 = i-1번째 계단에 두 칸 올라온 경우 + 이번 계단 점수
         = dp[i-1][1]+steps[i]
dp[i][1] = 계단을 두 칸 올라와서 얻는 점수 = i-2번째 계단에 아무렇게나 올라와도 상관이 없다
         = max(dp[i-2])+steps[i] 
'''
input = open(0).readline

def solution(n,steps):
    if n == 1 :
        return steps[1]
    if n == 2 :
        return steps[1]+steps[2]
    dp = [[0]*2 for _ in range(n+1)] # 시작점 포함 계단마다 얻는 최대 점수 dp 생성
    dp[1],dp[2] = [steps[1],0],[steps[1]+steps[2],steps[2]]
    for i in range(3,n+1): # 시작점 제외하고 첫번째 칸부터 시작
        tmp_step = steps[i]
        dp[i][0] = dp[i-1][1]+tmp_step # 한 칸 올라온 경우
        dp[i][1] = max(dp[i-2])+tmp_step # 두 칸 올라온 경우
    return max(dp[-1])

if __name__ == '__main__':
    n = int(input())
    steps = [0]+[int(input()) for _ in range(n)] # 인덱스를 맞추기 위해 0추가
    print(solution(n,steps))