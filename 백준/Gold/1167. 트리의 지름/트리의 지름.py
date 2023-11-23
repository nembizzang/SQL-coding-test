'''
트리 구조에서 임의의 한 노드로부터 가장 멀리 떨어진 노드는 반드시 트리의 지름 중 한 노드이다.
따라서 임의의 한 노드부터 가장 멀리 떨어진 노드를 구하고 그 노드로부터 가장 멀리 떨어진 노드까지의 거리를 구하자.
1) 다익스트라 함수 생성
def dikstra(node):
    shortcut = [노드별 최단거리] : 처음에는 inf
    shortcut[node] = 0 : 자기 자신까지 거리는 0
    queue = [[0,1]] # 시작 노드는 1로 임의로 지정
    heapify(queue)
    while 문 : queue 빌 때까지
        cur_dist,cur_node = heappop(queue)
        cur_node의 현재 최단거리가 현재 이동거리보다 짧으면 continue
        for 문 : tree[cur_node]에서 new_node,dist 반복
            if 문 : new_node의 현재 최단거리가 추가 이동거리보다 길면
                shortcut[new_node] 최신화
                queue에 dist+cur_dist, new_node heappush
    return shortcut

2) 입력값 받기 & 변수 선언
v = 정점의 개수
tree = {노드:[간선으로 이어진 노드, 거리]}

3) 다익스트라 2회 진행 - 지름 노드 중 한 점 찾고 다익스트라 한번 더 진행
shortcut = dikstra(1)
diameter_node = shortcut.index(max(shortcut))
return max(dikstra(diameter_node))
'''
from collections import defaultdict
from heapq import heapify, heappush, heappop

input = open(0).readline

def dikstra(node):
    shortcut = [-1]*(v+1) # 처음에는 -1
    shortcut[node] = 0 # 자기 자신까지 거리는 0
    queue = [[0,node]] # 시작 노드 지정
    heapify(queue)
    while queue :
        cur_dist,cur_node = heappop(queue)
        if shortcut[cur_node] != -1 and shortcut[cur_node] < cur_dist :
            continue
        for new_node,dist in tree[cur_node]:
            if shortcut[new_node]==-1 or shortcut[new_node] > cur_dist+dist :
                shortcut[new_node] = cur_dist+dist
                heappush(queue,[cur_dist+dist, new_node])
    return shortcut

def solution():
    global v, tree
    # 2) 입력값 받기 & 변수 선언
    v = int(input())
    tree = defaultdict(list)
    for _ in range(v):
        node,*graph,_ = list(map(int,input().split()))
        for i in range(len(graph)//2) :
            tree[node].append(graph[2*i:2*i+2])

    # 3) 다익스트라 2회 진행 - 지름 노드 중 한 점 찾고 다익스트라 한번 더 진행
    shortcut = dikstra(1)
    diameter_node = shortcut.index(max(shortcut))
    return max(dikstra(diameter_node))

if __name__ == '__main__':
    print(solution())