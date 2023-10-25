'''
연속된 수들의 부분합을 확인하며 그 합이 s이상이 되는 것 중 가장 짧은 것의 길이를 구하면 된다.
1. 투 포인터 초기화 : left=right=0
2. 최소 길이 min_len = n+1, 현재 합 cnt 초기 값 = nums[0]
3. while문 :
        if cnt < s : 현재 합이 s 미만이라면
            만약 right가 마지막인덱스인데도 s미만이면 break
            right += 1, cnt에 right 추가, s 이상될 때까지 continue
        # s 이상이 되어서 위 if 문을 반복하지 않는다면
        min_len = min(min_len,right-left+1) : # 새로운 최소길이 초기화
        cnt에 left값 빼주고 left값 +1
4. while 문 탈출 후 min_len <= n 이라면 min_len 출력, 아니면 0출력
'''
input = open(0).readline
def solution():
    n,s = map(int,input().split())
    nums = list(map(int,input().split()))
    if sum(nums) < s :
        return 0
    left=right=0 # 투 포인터 초기화
    min_len,cnt = n+1, nums[0] # 최소 길이, 현재 합 초기화
    if cnt >= s:
        return 1
    while True :
        if cnt < s : # 현재 합이 s미만이라면
            if right == n-1 : # 만약 끝에 도달했는데도 합이 s미만이라면
                break
            right+=1 # 현재 합 늘어나는 방향으로 진행
            cnt += nums[right]
            continue
        # s 이상이 되어서 위 if 문을 반복하지 않는다면
        min_len = min(min_len, right-left+1) # 새로운 최소 길이 초기화
        cnt -= nums[left]
        left += 1
    return min_len

if __name__ == '__main__':
    print(solution())