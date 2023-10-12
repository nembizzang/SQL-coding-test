'''
현재 줄을 stack라고 하자.
while 문 range(1, 마지막 학생번호) 진행
nums[0]이 i와 같다면 다음 while문 진행
i와 다르고 i==wait_stack[-1] 이라면 wait_stack.pop()하고 다음 while문 진행
둘 다 아니라면 stack.pop(0)값을 대기열 wait_stack에 append
while 문이 종료되었는데 wait_stack이나 stack가 남아있다면 실패
'''
input = open(0).readline

def solution(n,nums):
    wait_stack = [] # 후보 대기열
    i = 1
    while i <= n : # 대기열 번호가 n보다 크면 종료
        if nums and i == nums[0] : # 현재 대기열이 있고, 원래 순서와 같다면
            nums.pop(0) # 현재 대기열 맨 앞 순서 통과
            i += 1 # 대기열 순서 넘기기
        elif wait_stack and i == wait_stack[-1]: # 후보 대기열이 있고 맨 앞 순서와 같다면
            wait_stack.pop()
            i += 1 # 대기열 순서 넘기기
        elif nums : # 어느 대기열의 순서도 맞지 않는데 현재 대기열이 있다면
            wait_stack.append(nums.pop(0)) # 현재 대기열에서 후보 대기열로 넘어가기
        else : # 어느 대기열의 순서도 맞지 않고 현재 대기열도 없다면
            break
    return 'Sad' if nums or wait_stack else 'Nice'

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    print(solution(n,nums))