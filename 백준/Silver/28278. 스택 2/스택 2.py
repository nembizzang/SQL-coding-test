input = open(0).readline

if __name__ == '__main__':
    n = int(input())
    stack = []
    for _ in range(n):
        ord = list(map(int,input().split()))
        if ord[0] == 1: stack.append(ord[1])
        elif ord[0] == 2: print(stack.pop() if stack else -1)
        elif ord[0] == 3: print(len(stack))
        elif ord[0] == 4: print(1 if not stack else 0)
        else : print(stack[-1] if stack else -1)