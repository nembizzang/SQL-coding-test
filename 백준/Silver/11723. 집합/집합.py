import sys

def solve():
    read = sys.stdin.readline
    m = int(read())
    all_s = (1 << 21) - 1
    s = 0
    div = 600_000
    for i in range(m // div):
        for _ in range(div):
            cmd = read().split()
            if cmd[0] == 'add':
                s |= (1 << int(cmd[1]))
            elif cmd[0] == 'remove':
                s &= ~(1 << int(cmd[1]))
            elif cmd[0] == 'check':
                print('1' if s & (1 << int(cmd[1])) else '0')
            elif cmd[0] == 'toggle':
                s ^= (1 << int(cmd[1]))
            elif cmd[0] == 'all':
                s = all_s
            elif cmd[0] == 'empty':
                s = 0
    for _ in range(m % div):
        cmd = read().split()
        if cmd[0] == 'add':
            s |= (1 << int(cmd[1]))
        elif cmd[0] == 'remove':
            s &= ~(1 << int(cmd[1]))
        elif cmd[0] == 'check':
            print('1' if s & (1 << int(cmd[1])) else '0')
        elif cmd[0] == 'toggle':
            s ^= (1 << int(cmd[1]))
        elif cmd[0] == 'all':
            s = all_s
        elif cmd[0] == 'empty':
            s = 0

solve()
