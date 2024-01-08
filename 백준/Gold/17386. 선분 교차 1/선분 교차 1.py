'''
벡터 외적을 활용한 CCW 알고리즘을 활용하여 구할 수 있다.
하나의 기준 선분과 기준 선분의 한 점과 다른 선분의 각 끝 점이 이루는 두개의 벡터 쌍의 외적을 각각 구한다.
이 두 외적 벡터가 각각 다른 방향이라면 교차를 하게된다.(두 외적 벡터의 곱이 음수)
그러나 교차하지는 않으나 이루는 각의 방향이 다른 경우가 있다.
이런 경우라면 기준 선분에 따라 한 번은 교차를, 한 번은 교차하지 않는 결과가 나온다.
따라서 기준 선분을 다른 선분으로 바꾼 상황에서 모두 교차하는지 확인해야한다.
'''
input = open(0).readline

def solution():
    xs,ys = [], [] # 모든 점의 x좌표와 y좌표
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
    print(1 if res1<0 and res2<0 else 0)

if __name__ == '__main__':
    solution()