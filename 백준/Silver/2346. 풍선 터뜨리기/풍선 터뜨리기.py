'''
숫자들을 deque 함수로 stack을 만들어서
rotate 메서드로 회전을 시킨 후 pop을 진행
deque의 rotate는 양수면 반시계방향회전이므로 문제 조건에 따라서는
-를 붙여줘야 양수일 때 인덱스가 커지는 쪽으로 이동한다.
풍선의 종이가 양수라면 : 풍선이 터진 순간 회전할 방향으로 풍선이 줄어있으므로 종이보다 1적게 이동하고
풍선의 종이가 음수라면 : 풍선이 터져도 회전할 방향의 풍선은 그대로이므로 종이대로 이동한다.
'''
from collections import deque
input = open(0).readline

def solution():
    ans = [] # 먼저 터지는 풍선 정답 배열
    stack = deque(range(1,n+1)) # 1번~n번까지 풍선 stack 만들기
    while stack :
        tmp = stack.popleft() # 풍선 터트리기
        ans.append(tmp) # 정답 배열에 터진 풍선 담기
        # 풍선이 터진 순간 인덱스가 -1씩 되므로 회전 이동은 절대값 -1 만큼
        mov = dic[tmp]-1 if dic[tmp] >= 0 else dic[tmp]
        stack.rotate(-mov) # 숫자만큼 회전(양수면 반시계방향으로 회전이므로 -붙여줌)
    return ans

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    dic = {i:nums[i-1] for i in range(1,n+1)} # 1~n번 풍선에 적혀있는 숫자대로 dictionary
    print(*solution())