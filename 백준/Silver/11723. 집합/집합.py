input = open(0).readline

def solution():
    s = [0]*21 # 1부터 20까지의 정수를 연산하기 위함
    for _ in range(int(input())):
        ord = input().split()
        if len(ord)==2 :
            x = int(ord[1])
        ord = ord[0]
        if ord == 'add':
            s[x] = 1
        elif ord == 'remove':
            s[x] = 0
        elif ord == 'check':
            print(1 if s[x] else 0)
        elif ord == 'toggle':
            s[x] = 0 if s[x] else 1
        elif ord == 'all':
            s = [1]*21
        else :
            s = [0]*21
            
if __name__ == '__main__':
    solution()