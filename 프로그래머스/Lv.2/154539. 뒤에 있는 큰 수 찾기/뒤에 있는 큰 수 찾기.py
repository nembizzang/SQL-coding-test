'''
stack에 0을 채우고 시작
numbers[1]부터 for 반복문으로 하나씩 확인
이번 num이 stack[0]보다 작으면 해당 num의 인덱스도 stack appendleft. (제일 오른편 수의 뒷 큰수부터 찾아야하므로)
이번 num이 stack[0]보다 크면 stack이 비거나 stack[0]이 num보다 클 때까지 ans[stack.popleft] = num
for 문이 종료되고 stack에 남은 인덱스들은 뒷 큰수를 못 찾았으므로 -1로 넣어준다.
'''
from collections import deque
def solution(numbers):
    ans = [0]*len(numbers)
    stack = deque([])
    for i in range(len(numbers)):
        num = numbers[i]
        while stack and numbers[stack[0]] < num: # stack이 비어있지 않고 num이 제일 오른쪽 수의 뒷 큰수가 될 수 있다면
            ans[stack.popleft()] = num
        stack.appendleft(i)
    while stack: # 뒷 큰수를 찾지 못한 수들이 stack에 남아있다.
        ans[stack.popleft()] = -1
    return ans