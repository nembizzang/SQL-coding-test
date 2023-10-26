'''
meet in the middle 알고리즘 활용
1. stuff를 반으로 나누어 각각의 모든 부분집합의 합을 구한다. (a_sum, b_sum)
2. 이분탐색을 위해 b_sum을 오름차순 정렬
3. a_sum에서 하나씩 꺼내어 c이하면 진행
   b_sum의 원소 중 둘의 합이 c이하인 최대값을 이분탐색으로 찾는다
   찾은 인덱스+1만큼 정답에 추가
'''
from itertools import combinations
input = open(0).readline

def solution():
    n,c = map(int,input().split())
    if not c :
        return 1 # c가 0이면 방법이 없음
    stuff = [int(i) for i in input().split() if int(i) <= c] # c보다 큰 물건은 어차피 못넣으므로 제외
    if not stuff :
        return 1 # 모두 다 안 넣는 경우밖에 없음
    ans = 0
    # stuff을 반으로 나누어 모든 부분집합의 합 구하기
    a_stuff, b_stuff = stuff[:len(stuff)//2], stuff[len(stuff)//2:]
    def make_subset(stuff):
        # 공집합의 경우를 위해 0을 미리 넣어두자
        sum_stuff = [0]
        for i in range(1,len(stuff)+1): # 1개부터 n개까지 뽑는 모든 조합
            for combi in combinations(stuff,i):
                sum_stuff.append(sum(combi))
        return sum_stuff
    a_sum,b_sum = make_subset(a_stuff), make_subset(b_stuff)

    # b_sum 오름차순 정렬
    b_sum.sort()

    # b_sum에서 c이하의 최대값 인덱스 구하는 이분탐색
    def binary_search(b_sum,c):
        left,right = 0, len(b_sum)-1
        while left<=right :
            mid = (left+right)//2
            if b_sum[mid] <= c :
                left = mid+1 # 커지는 방향
            else :
                right = mid-1 # 작아지는 방향
        return right+1
    
    # a_sum에서 하나씩 꺼내서 확인
    for a_subset in a_sum:
        if a_subset <= c:
            ans+= binary_search(b_sum,c-a_subset) # 전체 합이 c-a_subset 이하인 최대 인덱스
    
    return ans

if __name__=='__main__':
    print(solution())