'''
1. 각 노드별로 x 노드까지 가는데 걸리는 거리를 다익스트라로 구하여
   리스트 형태로 담아두기
2. x 노드부터 출발하여 각 노드까지 가는 거리를 다익스트라로 구하여
   리스트 형태로 담아두기
3. 두 리스트를 합하여 최댓값 구하기
다익스트라 함수를 만들고 flag에 따라 반환하는 종류를 두가지로 나누자.
1) 각 노드별 x까지의 거리 값
2) x로부터 각 노드까지 거리 리스트
'''
from heapq import heapify, heappush, heappop
input = open(0).readline

def solution():
    n,m,x = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        sta,end,dist = map(int,input().split())
        graph[sta].append([end,dist])
    to_go = [0]*(n+1) # 출발노드부터 x노드까지의 거리
    # 다익스트라로 출발 노드별로 x노드까지의 거리를 반환
    def dikstra(sta,flag=True): # flag=False면 x노드로부터 각 노드까지 거리 리스트를 반환
        if sta==x and flag : # 가는 길인데 출발노드가 x 라면
            return 0
        short_cut = [float('inf')]*(n+1)
        short_cut[sta] = 0
        queue = [(0,sta)]
        heapify(queue) # 경로,도착노드
        while queue:
            cur_dist,cur_node = heappop(queue)
            if short_cut[cur_node] < cur_dist : # 현재 이동거리가 현재 최단거리보다 크면
                continue
            for new_node,new_dist in graph[cur_node]:
                if short_cut[new_node] > cur_dist+new_dist : # new_node까지 최단거리를 갱신할 수 있다면
                    short_cut[new_node] = cur_dist+new_dist
                    heappush(queue,(cur_dist+new_dist,new_node))
        if flag :
            return short_cut[x] # 가는 길의 경우 x 노드까지 거리값 반환
        return short_cut # 오늘 길의 경우 x노드로부터 모든 노드까지 거리리스트 반환
    
    # x로 갈때 최단거리 구하기
    for sta in range(1,n+1):
        to_go[sta] = (dikstra(sta))
    # x에서 돌아올때 최단거리 구하기
    comeback = dikstra(x,False)
    ans = 0
    for go,come in zip(to_go,comeback):
        if go != float('inf') and come != float('inf'):
            ans = max(ans,go+come)
    return ans

if __name__ == '__main__':
    print(solution())