'''
설정하는 높이가 h이고 나무의 높이가 tree일때 상근이가 가져가는 나무 길이 l
l = tree - h if tree > h else 0
h를 0에서 max(trees)까지 이분 탐색하며 나무 길이가 m 이상인 지점을 찾자
똑같은 높이의 나무에 대해서는 여러번 연산해줄 필요없이 개수를 곱해주자(Counter 사용)
'''
from collections import Counter
input = open(0).readline

def solution(m,trees):
    counter = Counter(trees)
    left,right = 0, 1000000000 # 이분 탐색의 시작과 끝
    while left<=right :
        mid = (left+right)//2 # 중간
        # 나무 높이 하나씩을 꺼내서 자른 길이를 더해준다.
        tmp_m = sum([(key-mid)*value for key,value in counter.items() if key>mid])
        if tmp_m >= m : # 나무 길이가 m이상일때
            left = mid+1
        else : # 나무 길이가 m미만일때
            right = mid-1
    return right # while 문을 빠져나오는 순간이 나무 길이가 m이상인 지점이므로

if __name__ == '__main__':
    n,m = map(int,input().split())
    trees = map(int,input().split())
    print(solution(m,trees))