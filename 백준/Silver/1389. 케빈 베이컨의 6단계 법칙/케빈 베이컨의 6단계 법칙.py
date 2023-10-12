from collections import defaultdict, deque
input = open(0).readline

def bacon(x) :
    tmp_dic = {i:-1 for i in range(1,n+1)} # 노드 방문 여부(-1이면 미방문)
    stack = deque([[x,0]]) # x 노드 방문, 방문까지 이동 경로(최초는 0)
    while stack :
        node,mov_cnt = stack.pop()
        if tmp_dic[node] == -1 or tmp_dic[node] > mov_cnt : # 최초 방문이거나 더 짧은 경로를 찾았다면
            tmp_dic[node] = mov_cnt # 방문 횟수 갱신
            for new_node in dic[node] : # 간선으로 이어지는 새로운 노드들
                stack.append([new_node,mov_cnt+1]) # 새로운 노드와 방문까지 이동 경로
    # 모든 노드 확인 완료 시
    return(sum(tmp_dic.values()))

def solution(n,tree):
    global dic
    dic = defaultdict(list) # 각 노드별 이어지는 간선 배열의 집합
    for a,b in tree:
        dic[a].append(b)
        dic[b].append(a)
    num_bacon = float('inf')
    bacon_node = 0
    for i in range(1,n+1):
        tmp_bacon = bacon(i)
        if num_bacon > tmp_bacon : # 베이컨 수가 작은 사람을 찾았다면
            num_bacon,bacon_node = tmp_bacon,i
    return bacon_node

if __name__ == '__main__':
    n,m = map(int,input().split())
    tree = [list(map(int,input().split())) for _ in range(m)]
    print(solution(n,tree))