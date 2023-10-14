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
from heapq import heappop, heappush
input = open(0).readline

def solution(sta): # 시작 노드로부터 다익스트라 bfs 진행
    short_cut[sta] = 0 # 시작 노드까지 최단 경로는 0
    queue = []
    heappush(queue,[0,sta]) # 확인할 노드를 담는 queue에 [최단 경로(0),출발노드] 담기
    while queue :
        cur_dist,cur_node = heappop(queue) # queue에서 현재 최단 경로와 확인할 노드 뽑기
        if short_cut[cur_node] < cur_dist : # cur_node의 현재 최단 경로가 현재의 경로보다 짧다면
            continue # 확인할 필요없이 다음 노드 확인 진행
            # 위 경우는 다음과 같은 경우에 작동한다.
            # 맨 처음에 1->2 : 비용 10인 간선을 확인하고 큐에 넣는다.
            # 직후에 1->3 : 4 / 3->2 : 2인 간선을 확인했다면 2까지의 최소비용은 6으로 들어가있다.
            # 나중에 비용 10, 출발 노드 2를 큐에서 뽑는다면 이미 이 상태에서는 최소비용보다 초과해있기에 아래 for문을 안해도 된다.
        for new_node,dist in path[cur_node] : # 현재 노드에서 간선으로 이어진 노드와 경로
            if short_cut[new_node] > cur_dist+dist : # new_node의 현재 최단 경로가 cur_node를 거쳐간 경로 보다 크다면
                short_cut[new_node] = cur_dist+dist # 최단 경로 갱신
                heappush(queue,[cur_dist+dist,new_node]) # 확인할 노드에 new_node 추가
    return # 모든 노드를 확인했다면 종료

if __name__ == '__main__':
    v,e = map(int,input().split()) # 정점 개수, 간선 개수
    k = int(input())
    path = [[] for _ in range(v+1)] # 노드의 인덱스에 [이웃 노드, 가중치] 모두 포함
    for i in range(e): # path 추가
        sta,end,w = map(int,input().split())
        path[sta].append([end,w])
    inf = float('inf')
    short_cut = [inf]*(v+1) # 각 노드까지 최단경로 저장할 list
    solution(k) # 시작점부터 bfs 시작
    for i in range(1,v+1):
        print(short_cut[i] if short_cut[i] != float('inf') else 'INF')