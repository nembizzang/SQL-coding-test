import sys
sys.setrecursionlimit(10**6)
input = open(0).readline

def solution():
    n,m = map(int,input().split())
    parents = list(range(n+1)) # 같은 집합에 포함된 수중 최소값
    
    def union(a,b): # 합집합 연산
        a, b = find(a), find(b) # a,b가 포함된 집합의 최소값 가져오기
        if a != b : # 이미 같은 집합이라면 통과
            if a < b : # 더 작은 쪽으로 맞추기
                parents[b] = a
            else : 
                parents[a] = b
    
    def find(a): # a가 포함된 집합의 최소값으로 parents 바꾸고 반환
        if a != parents[a] : # a가 자신이 포함된 집합의 최솟값이 아니라면
            parents[a] = find(parents[a]) # parents[a]가 포함된 집합의 최소값 초기화
        return parents[a] # a가 포함된 집합의 최소값 반환
    
    for _ in range(m):
        operation, a, b = map(int,input().split())
        if operation : # 같은 집합에 속했는지 확인
            print('YES' if find(a) == find(b) else 'NO')
        else : # 합집합 연산
            union(a,b)
    
    print(parents)
            
if __name__ == '__main__':
    solution()