from collections import defaultdict
from heapq import heapify, heappush, heappop
input = open(0).readline

def dikstra(sta): # 다익스트라 함수
    short_cut = [float('inf') for _ in range(n+1)]
    short_cut[sta] = 0
    queue = [[0,sta]]
    heapify(queue) # 경로,도착노드
    while queue:
        cur_dist,cur_node = heappop(queue)
        if short_cut[cur_node] < cur_dist : # 현재 이동거리가 현재 최단거리보다 크면
            continue
        for new_node,new_dist in graph[cur_node]:
            if short_cut[new_node] > cur_dist+new_dist : # new_node까지 최단거리를 갱신할 수 있다면
                short_cut[new_node] = cur_dist+new_dist
                heappush(queue,[cur_dist+new_dist,new_node])
    return short_cut

def solution():
    global n, graph
    graph = defaultdict(list)
    n,m,x = map(int,input().split())
    for _ in range(m):
        sta,end,dist = map(int,input().split())
        graph[sta].append([end,dist])
    # x로 갈때 최단거리 구하기
    short_cut = [0] # 다익스트라 결과를 담아줄 리스트
    for i in range(1,n+1):
        short_cut.append(dikstra(i))
    for i in range(1,n+1):
        short_cut[x][i] += short_cut[i][x]
    return max(short_cut[x][1:])

if __name__ == '__main__':
    print(solution())