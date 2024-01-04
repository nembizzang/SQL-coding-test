'''
선분의 진행 방향이 어느 방향으로 바뀌었는지 확인하는 문제이다.
두 벡터의 외적을 구하는 공식을 활용한 CCW(counter clock wise) 알고리즘으로 풀 수 있다.

두 벡터의 외적의 크기는 두 벡터가 만드는 평행사변형의 넓이와 같고
방향은 두 벡터와 모두 수직하며, 사이각에 따라서 그 부호가 결정된다.
따라서 벡터의 부호에 따라서 두 선분이 이루는 방향을 구할 수 있다.
AxB = absin(angle)이라는 외적 공식을 활용하자.
'''
input = open(0).readline

def solution():
    def ccw(s1,s2,s3): # 외적의 크기를 구하는 공식
        return (s1[0]*s2[1]+s2[0]*s3[1]+s3[0]*s1[1])-(s2[0]*s1[1]+s1[0]*s3[1]+s3[0]*s2[1])
    
    spots = [list(map(int, input().split())) for _ in range(3)] # 세 개의 점
    ex = ccw(*spots) # 외적 결과
    if ex > 0 : # 반시계 방향
        print(1)
    elif ex == 0 : # 일직선
        print(0)
    else : # 시계 방향
        print(-1)

if __name__ == '__main__':
    solution()