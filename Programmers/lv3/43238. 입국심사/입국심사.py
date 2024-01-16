# 이진탐색 : chk = sum([x//time for time in times])
# 최소값 : 조건문은 right = mid-1 쪽에, left값 출력
def solution(n, times):
    left, right = 0, max(times)*n
    while left <= right :
        mid = (left+right)//2
        if n <= sum([mid//time for time in times]) : # chk할 시간을 줄여야한다면
            right = mid-1
        else :
            left = mid+1
    return left