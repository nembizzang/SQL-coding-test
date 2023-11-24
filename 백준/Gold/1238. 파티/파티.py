'''
1. x로 가는 경로 구하기
   다른 노드에서 x로 가는 경로를 구할 때는 간선 정보의 출발, 도착을 거꾸로 입력받는다.
   이를 통해 x에서 각 노드간의 거리를 한번의 다익스트라로 구하여 리스트 형태로 저장
2. x에서 돌아오는 경로 구하기
   x 노드부터 출발하여 각 노드까지 가는 거리를 다익스트라로 구하여 리스트 형태로 저장
3. 두 리스트를 합하여 최댓값 구하기
다익스트라 함수를 만들고 flag에 따라 반환하는 종류를 두가지로 나누자.
'''
from heapq import heapify, heappush, heappop
input = open(0).readline

def solution():
    n,m,x = map(int,input().split())
    go_graph = [[] for _ in range(n+1)]
    come_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        sta,end,dist = map(int,input().split())
        go_graph[end].append([sta,dist])
        come_graph[sta].append([end,dist])
    # 다익스트라로 출발 노드별로 x노드까지의 거리를 반환
    def dikstra(graph):
        inf = float('inf')
        short_cut = [inf]*(n+1)
        short_cut[0] = short_cut[x] = 0 # 0노드(안씀)와 x노드 = 0
        queue = [(0,x)]
        heapify(queue) # 경로,도착노드
        while queue:
            cur_dist,cur_node = heappop(queue)
            if short_cut[cur_node] < cur_dist : # 현재 이동거리가 현재 최단거리보다 크면
                continue
            for new_node,new_dist in graph[cur_node]:
                if short_cut[new_node] > cur_dist+new_dist : # new_node까지 최단거리를 갱신할 수 있다면
                    short_cut[new_node] = cur_dist+new_dist
                    heappush(queue,(cur_dist+new_dist,new_node))
        return short_cut
    
    # x로 갈때, 올때 최단거리 구하기
    to_go, comeback = dikstra(go_graph), dikstra(come_graph)
    ans = 0
    for go,come in zip(to_go[1:],comeback[1:]):
        ans = max(ans,go+come)
    return ans

if __name__ == '__main__':
    print(solution())