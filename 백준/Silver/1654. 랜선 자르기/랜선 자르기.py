'''
각 랜선의 원래 길이를 l, 자를 길이를 c라고 한다면 랜선 개수는 l//c이다.
이들의 합이 n개 이상이 되는 최대의 c를 구해야하므로
1부터 랜선 원래 길이 중 최대값까지를 이분 탐색해가며 c를 찾아내자
'''
input = open(0).readline
def solution():
    left,right = 1,max(lans) # 이분 탐색 최초 처음과 끝 설정
    while left<=right :
        mid = (left+right)//2 # 중간값
        cnt_lans = 0 # 랜선의 총 개수
        for lan in lans:
            cnt_lans+= lan//mid
        if cnt_lans >= n : # 필요한 개수가 타겟값 이상이라면
            left = mid+1 # 개수를 줄이려면 길이는 길어져야함
        else :
            right = mid-1
    # while문을 탈출할 때 마지막 동작은 right = mid-1이다.
    # 왜냐하면 mid = (left+right)//2이기 때문에 mid+1은 right를 초과할 수 없고
    # right가 mid=left일 때 1이 작아져야 탈출할 수 있기 때문
    # 따라서 이 때의 right가 cnt_lans < n인 최대 길이이므로
    # 
    return right 

if __name__ == '__main__':
    k,n = map(int,input().split())
    lans = [int(input()) for _ in range(k)]
    print(solution())