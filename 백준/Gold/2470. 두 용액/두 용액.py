'''
두가지 용액의 특성값을 합했을 때 0과 가장 가까운 두 용액을 찾아야한다.
1. nums(특성값) 오름차순 정렬
2. 투 포인터 지정 : left = 0, right = n-1 (인덱스 값)
3. 최소값 min_sum = float('inf'), 두 용액 ans = [] 지정
3. while문 : left < right 동안 nums[left]+nums[right] 확인
            if 합이 0이다 :
                return nums[left],nums[right]
            if 합의 절대값이 min_sum보다 작다 :
                min_sum, ans 두 용액으로 초기화
            if 합이 음수면 left+1, 양수면 right-1
'''
input = open(0).readline
def solution():
    n = int(input())
    nums = sorted(list(map(int,input().split())))
    left,right = 0,n-1 # 투 포인터 초기화
    min_sum = float('inf') # 특성값합 최소값
    ans = [] # 두 용액
    while left < right :
        tmp=nums[left]+nums[right] # 현재 특성값의 합
        if not tmp : # 합이 0이면
            return nums[left],nums[right] # 정답 바로 출력 후 종료
        if min_sum > abs(tmp) : # 최소값을 찾았다면
            min_sum = abs(tmp)
            ans = [nums[left], nums[right]]
        if tmp < 0 : # 합이 음수면
            left += 1 # 용액 특성값이 커지는 방향으로 포인터 이동
        else :
            right -= 1 # 용액 특성값이 작아지는 방향으로 포인터 이동
    return ans

if __name__ == '__main__':
    print(*solution())