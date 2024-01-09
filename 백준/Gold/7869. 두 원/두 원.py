'''
제 2 코사인 법칙을 활용해 각도를 구해서 넓이를 구하는데 사용
'''
from math import dist, pi, acos, sin
input = open(0).readline

def solution():
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    if (x1-x2)**2 + (y1-y2)**2 >= (r1+r2)**2:
        print('0.000')
    else:
        d = dist((x1, y1),(x2, y2))
        if d + min(r1, r2) <= max(r1, r2):
            r = min(r1, r2)
            total = pi*r*r
        else:
            theta1 = 2*acos((r1*r1+d*d-r2*r2)/(2*r1*d))
            theta2 = 2*acos((r2*r2+d*d-r1*r1)/(2*r2*d))
            total = r1*r1*(theta1-sin(theta1))/2 + r2*r2*(theta2-sin(theta2))/2
        print(f'{round(total, 3):.3f}')

if __name__ == '__main__':
    solution()