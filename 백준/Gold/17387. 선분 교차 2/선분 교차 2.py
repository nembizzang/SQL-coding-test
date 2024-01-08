'''
선분 교차1의 문제에 한 선분의 끝 점이 다른 선분 위에 있는 경우도 교차하는 것으로 포함하는 문제이다.
일직선에 놓인 세 점의 외적은 0이므로 이 조건을 추가해주자.
이때 두 선분이 일직선 위에 있는 경우에는 모두 외적이 0이지만 겹치지 않을 경우도 있다.
기준 선분을 바꿔도 외적 벡터 쌍의 곱이 모두 0인 경우에 일직선이다.
이 경우에서 겹치는 조건을 확인하는 방법은 다음과 같다.
선분12과 선분34 각 점의 x,y 평균을 m1,m2,m3,m4라고 하자.
min(m1,m2) >= max(m3,m4) or max(m1,m2) <= min(m3,m4)라면 겹치 경우이다.
'''
input = open(0).readline

def solution():
    xs,ys = [],[] # 모든 점의 x좌표와 y좌표
    for _ in range(2):
        x1,y1,x2,y2 = map(int, input().split())
        xs += [x1,x2]
        ys += [y1,y2]

    def ccw(xs,ys): # 세 점의 x좌표와 y좌표
        res = 0
        for i in range(3):
            res += xs[i]*ys[(i+1)%3] - xs[(i+1)%3]*ys[i]
        return res
    
    # 기준 선분을 바꿔가며 교차 확인
    res1 = ccw(xs[:2]+[xs[2]],ys[:2]+[ys[2]])*ccw(xs[:2]+[xs[3]],ys[:2]+[ys[3]])
    res2 = ccw(xs[2:4]+[xs[0]],ys[2:4]+[ys[0]])*ccw(xs[2:4]+[xs[1]],ys[2:4]+[ys[1]])

    if res1 == res2 == 0 : # 네 점이 일직선인 경우
        mx1, my1, mx2, my2 = min(xs[0], xs[1]), min(ys[0], ys[1]), max(xs[0], xs[1]), max(ys[0], ys[1])
        mx3, my3, mx4, my4 = min(xs[2], xs[3]), min(ys[2], ys[3]), max(xs[2], xs[3]), max(ys[2], ys[3])
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    elif res1 <= 0 and res2 <= 0 : # 교차하거나 세 점이 일직선인 경우
        return 1 # 교차하거나 세 점이 일직선
    return 0 # 교차하지 않는 경우

if __name__ == '__main__':
    print(solution())