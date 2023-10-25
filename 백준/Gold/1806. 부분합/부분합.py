'''
연속된 수들의 부분합을 확인하며 그 합이 s이상이 되는 것 중 가장 짧은 것의 길이를 구하면 된다.
1. 투 포인터 초기화 : left,right=0,1
2. 최소 길이 min_len = n+1, 현재 합 cnt 초기 값 = nums[left:right+1]
3. while문 : right가 nums 인덱스를 초과하면 종료
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
    left=right=0 # 투 포인터 초기화
    min_len,cnt = n+1, nums[0] # 최소 길이, 현재 합 초기화
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
    return min_len if min_len<=n else 0

if __name__ == '__main__':
    print(solution())