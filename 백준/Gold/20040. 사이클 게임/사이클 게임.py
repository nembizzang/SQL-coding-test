'''
find 함수로 해당 노드와 이어진 최소 노드를 찾아 parents에 넣고, union 함수로 같은 parents를 만들어준다.
두개 노드씩 입력값을 받으면서 두 노드의 parents가 이미 같다면 사이클이 처음으로 완료되는 지점이다.
두 노드의 parents가 다르다면 union을 계속 진행한다.
'''
input = open(0).readline

def solution():
    def find(a): # 해당 노드와 이어진 최소 노드 찾기
        if a != parents[a]:
            parents[a] = find(parents[a])
        return parents[a]
    
    def union(a,b) : # 이어진 노드간 같은 parents 만들기
        a,b = find(a),find(b)
        if a == b : # union 이전 이미 같은 노드라면
            return True # 사이클 완성
        if a < b : # b가 더 크면
            parents[b] = a # 작은 값으로 parents 맞추기
        else :
            parents[a] = b 
        return False # 사이클 미완성
    
    n,m = map(int, input().split())
    parents = list(range(n+1)) # 해당 인덱스와 이어진 노드의 최소값
    for i in range(1,m+1) :
        a,b = map(int,input().split())
        if union(a,b) :
            return i
    return 0 # 사이클이 완성되지 않았다면 0 반환

if __name__ == '__main__':
    print(solution())