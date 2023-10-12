from collections import Counter
input = open(0).readline

def solution(n,nums):
    # key point : 시간복잡도를 줄이기위해 반복을 줄여야한다.
    # 한 인덱스를 확인할 때마다 더 큰 등장횟수를 찾기 위해 뒤의 인덱스들을 매번 확인하는 것은 비효율적
    # for 문을 한번만 돌면서 지금 확인하는 인덱스의 숫자가 이전 인덱스들의 오등큰수가 될 수 있는지를 확인하자
    # 오등큰수를 찾지 못한 인덱스를 인덱스 순서대로 stack에 넣고 확인되는 순간 pop 시켜주자
    ans = [-1]*n
    counter = Counter(nums)
    stack = [0] # 맨 처음 인덱스
    for i in range(1,n) : # 인덱스 1부터 확인
        tmp_num = nums[i]
        # stack에는 stack의 마지막 인덱스의 수보다 등장횟수가 작은 인덱스들이 들어간다(등장횟수 내림차순 정렬)
        # 따라서 stack 마지막 인덱스 수의 등장횟수보다 등장횟수가 큰 수를 가진 인덱스를 찾아도
        # 이전 인덱스의 오등큰수는 아닐 수 있기에 while 문으로 진행한다.
        while stack and counter[nums[stack[-1]]] < counter[tmp_num] : # stack 마지막 인덱스의 오등큰수를 발견했다면
            ans[stack.pop()] = tmp_num # stack 마지막 인덱스의 오등큰수는 현재 인덱스의 수
        stack.append(i) # 이전 인덱스들을 모두 확인해줬다면 지금 숫자의 인덱스 추가
    return ans

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    print(*solution(n,nums))