'''
설정하는 높이가 h이고 나무의 높이가 tree일때 상근이가 가져가는 나무 길이 l
l = tree - h if tree > h else 0
h를 0에서 max(trees)까지 이분 탐색하며 나무 길이가 m 이상인 지점을 찾자
'''
input = open(0).readline

def solution(m,trees):
    left,right = 0, max(trees) # 이분 탐색의 시작과 끝
    while left<(left+right)//2 :
        mid = (left+right)//2 # 중간
        # 설정 높이가 mid일때 가져가는 나무 길이 tmp_m
        tmp_m = sum([tree-mid if tree>mid else 0 for tree in trees])
        if tmp_m >= m : # 나무 길이가 m이상일때
            left = mid
        else : # 나무 길이가 m미만일때
            right = mid
    return left # while 문을 빠져나오는 순간이 나무 길이가 m이상인 지점이므로

if __name__ == '__main__':
    n,m = map(int,input().split())
    trees = list(map(int,input().split()))
    print(solution(m,trees))