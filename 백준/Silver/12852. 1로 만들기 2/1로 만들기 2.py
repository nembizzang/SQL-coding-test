input = open(0).readline

def solution():
    n = int(input())
    dp = {1:0,2:1} # 숫자별 최소 도달 연산횟수를 담아줄 딕셔너리
    # i==2인 경우를 제외하면 -1로 이동하는 것이 최소인 경우는 없기에 1까지 도달할 때 /2,/3만 확인하면 된다.
    def shortcut(i):
        if i in dp : # i에 도달하는 최단 연산횟수를 이미 찾았다면 그 연산횟수를 반환
            return dp[i]
        # i에 도달하는 최단 경로는 나머지만큼 빼주고 /3 연산을 하거나 /2 연산을 해주는 경우
        dp[i] = 1 + min(shortcut(i//3)+i%3, shortcut(i//2)+i%2)
        return dp[i]
    print(shortcut(n)) # n까지 도달하는 최단 연산횟수를 반환

    while n!=1 : # n이 1에 도달할 때까지 최단 연산 경로를 출력
        print(n, end=' ') # 먼저 n을 출력
        if n-1 in dp and dp[n-1] == dp[n]-1 : # -1 연산으로 진행한 적이 있고 최단 연산 경로라면
            n -= 1
        elif n//3 in dp and dp[n//3] + n%3 == dp[n]-1 : # /3 연산으로 진행한 적이 있고 최단 연산 경로라면
            for _ in range(n%3) : # 나머지만큼 반복
                n -= 1 # 1빼고
                print(n, end = ' ') # 출력
            n //= 3 # 나누기 3 
        else : # /2 연산으로 진행한 적이 있고 최단 연산 경로라면
            for _ in range(n%2) : # 나머지만큼 반복
                n -= 1 # 1빼고
                print(n, end = ' ') # 출력
            n //= 2 # 나누기 2
    print(1) # 최종 도달지점인 1 출력
if __name__ == '__main__':
    solution()