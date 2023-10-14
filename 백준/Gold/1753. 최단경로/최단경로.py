'''
한 노드에서 다른 모든 노드까지의 최단 경로를 구하는 문제이기에 다익스트라 알고리즘
- 입력 : v(정점 개수), e(간선 개수), k(시작 정점), 노드별 도착 노드&가중치
1. bfs 진행(dijkstra)
    1-1. while 문 : queue에 확인할 노드가 있는동안 확인
        - 큐에서 노드와 가중치를 하나씩 뽑음(heappop으로 최단 경로 먼저 확인해서 시간 단축)
        - for 문 : 해당 노드에서 도착할 수 있는 노드들을 하나씩 가져와서 최단 경로 확인
            - 최단 경로라면 도착 노드까지 최단 경로 업데이트 및 큐에 추가
2. 정답 출력 : 정점별 최단경로 출력
'''
from collections import defaultdict
from heapq import heappop, heappush
input = open(0).readline

def solution(sta): # 시작 노드로부터 다익스트라 bfs 진행
    short_cut[sta] = 0 # 시작 노드까지 최단 경로는 0
    queue = []
    heappush(queue,[0,sta]) # 확인할 노드를 담는 queue에 [최단 경로(0),출발노드] 담기
    while queue :
        cur_dist,cur_node = heappop(queue) # queue에서 현재 최단 경로와 확인할 노드 뽑기
        for new_node,dist in path[cur_node] : # 현재 노드에서 간선으로 이어진 노드와 경로
            if short_cut[new_node] > cur_dist+dist : # new_node의 현재 최단 경로가 cur_node를 거쳐간 경로 보다 크다면
                short_cut[new_node] = cur_dist+dist # 최단 경로 갱신
                heappush(queue,[cur_dist+dist,new_node]) # 확인할 노드에 new_node 추가
    return # 모든 노드를 확인했다면 종료

if __name__ == '__main__':
    v,e = map(int,input().split()) # 정점 개수, 간선 개수
    k = int(input())
    path = defaultdict(list) # 출발 노드 : [[도착 노드, 가중치]]
    for _ in range(e): # path 추가
        sta,end,w = map(int,input().split())
        path[sta].append([end,w])
    inf = float('inf')
    short_cut = {i:inf for i in range(1,v+1)} # 각 노드까지 최단경로 저장할 dictionary
    solution(k) # 시작점부터 bfs 시작
    for i in range(1,v+1):
        print(short_cut[i] if short_cut[i] != float('inf') else 'INF')