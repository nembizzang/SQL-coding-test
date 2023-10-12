from collections import deque
input = open(0).readline

if __name__ == '__main__':
    stack = deque()
    for _ in range(int(input())):
        ord = list(map(int,input().split()))
        if ord[0]==1: stack.appendleft(ord[1])
        elif ord[0]==2: stack.append(ord[1])
        elif ord[0]==3: print(stack.popleft() if stack else -1)
        elif ord[0]==4: print(stack.pop() if stack else -1)
        elif ord[0]==5: print(len(stack))
        elif ord[0]==6: print(0 if stack else 1)
        elif ord[0]==7: print(stack[0] if stack else -1)
        else : print(stack[-1] if stack else -1)