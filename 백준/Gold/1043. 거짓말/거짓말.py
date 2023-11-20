from collections import defaultdict
input = open(0).readline

def solution():
    n,m = map(int,input().split())
    k,*known = list(map(int,input().split()))
    truman = defaultdict(int) # 모르면 0, 알면 1
    if not k : # 진실러가 없다면
        return m # 모든 파티 참가 가능
    else :
        for i in known :
            truman[i] = 1 # 진실러 업데이트
    party = []
    for t in range(m): # 모든 과정을 파티 수만큼 반복
        if not t : # 첫번째 시도라면
            for _ in range(m): # 모든 파티 확인
                _,*nums = list(map(int,input().split())) # 파티별 사람 리스트
                for i in nums :
                    if truman[i] == 1 : # 파티 중 한명이라도 진실을 알면
                        for j in nums :
                            truman[j] = 1 # 진실러 업데이트
                        break # 아는 사람이 나온 순간 전체 업데이트 후 탈출
                party.append(nums) # 파티별 참여자 업데이트
        else :
            for nums in party: # 모든 파티 확인
                for i in nums :
                    if truman[i] == 1 : # 파티 중 한명이라도 진실을 알면
                        for j in nums :
                            truman[j] = 1 # 진실러 업데이트
                        break # 아는 사람이 나온 순간 전체 업데이트 후 탈출
    # 모든 파티를 확인했다면
    ans = m
    for nums in party :
        for i in nums :
            if truman[i] == 1 : # 진실러가 한명이라도 있으면
                ans -= 1 # 그 파티는 참여 불가
                break # 다음 파티 확인
    return ans

if __name__ == '__main__':
    print(solution())