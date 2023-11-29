'''
tree={node:[자식노드]}로 만들어주고
bfs로 1번부터 자식노드로 내려가면서 각 자식노드에 대한 부모노드를 인덱스에 맞게 list로 반환

1) 변수 선언
n : 노드개수
tree = {node:[자식노드]}
parents = [0]*(노드개수+1)
visited = {node:방문여부}

2) bfs
stack = deque([1])
while stack :
    노드를 하나씩 꺼내서
    그 노드와 이어진 자식 노드를 하나씩 확인
    node에 방문한 적이 없다면
    visited에 방문 체크
    parents[자식노드]=부모노드로 초기화해주고 자식 노드를 stack에 넣어준다.

3) 결과 출력
parents[2:]부터 하나씩 출력
'''
from collections import deque,defaultdict
input = open(0).readline

def solution():
    # 변수 선언
    n = int(input())
    tree, visited = defaultdict(list), defaultdict(int)
    parents = [0]*(n+1)
    for _ in range(n-1): # node별 간선으로 이어주기
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    # BFS
    stack = deque([1]) # 시작 노드는 1
    while stack :
        p_node = stack.popleft()
        for c_node in tree[p_node]:
            if visited[c_node]: # node에 방문한 적이 있다면 통과
                continue
            visited[c_node] = 1
            parents[c_node] = p_node
            stack.append(c_node)
    # 결과 출력
    for i in parents[2:]:
        print(i)
if __name__ == '__main__':
    solution()