'''
벡터의 외적 계산을 통해 면적을 구하는 문제이다.
신발끈 공식을 활용해 풀 수 있다.
'''
input = open(0).readline

def solution():
    n = int(input())
    xs,ys = [],[]
    for _ in range(n):
        x,y = map(int,input().split())
        xs.append(x)
        ys.append(y)
    # 신발끈 공식을 활용한 계산
    def ccw(xs,ys): # n개의 점들의 x좌표, y좌표
        res = 0
        for i in range(n):
            res += xs[i]*ys[(i+1)%n] - xs[(i+1)%n]*ys[i]
        return res
    print(round(abs(ccw(xs,ys)/2),2)) # 방향을 제외한 절대값을 반올림

if __name__ == '__main__':
    solution()