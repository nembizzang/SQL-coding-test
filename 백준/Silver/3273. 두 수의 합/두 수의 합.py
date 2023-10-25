'''
1. 입력받은 nums를 오름차순 정렬해준다.
2. 두개의 포인터를 left=0와 right=n-1로 nums의 양쪽 끝 인덱스로 지정해준다.
3. while문 : nums[left]+nums[right]가 x인지 확인
             if x와 같다면 정답 +1, left+1, right-1, continue
             if x보다 작다면 left+1, continue
             if x보다 크다면 right-1, continue
'''
input = open(0).readline

def solution():
    n = int(input())
    nums = sorted(list(map(int,input().split())))
    x = int(input())
    left,right = 0,n-1
    cnt = 0 # 쌍의 수
    while left < right :
        tmp_x = nums[left] + nums[right]
        if x > tmp_x:
            left+=1
            continue
        if x == tmp_x :
            cnt+=1
        right-=1
    return cnt

if __name__ == '__main__':
    print(solution())