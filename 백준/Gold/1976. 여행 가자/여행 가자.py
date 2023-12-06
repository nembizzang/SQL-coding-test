'''
주어진 연결 정보들로 도시별 연결성을 나타내는 parents 리스트를 만들자.
parents = (인덱스+1)번호의 도시와 연결된 도시 중 가장 작은 번호의 도시
parents를 완성 후 여행계획을 살피며 모두 같은 parents 값을 가지고 있는지 확인하자.
이때 find와 union 함수를 통해 parents 리스트를 완성하자.
find : 해당 도시와 연결된 가장 작은 번호의 도시로 parents값을 초기화하고 그 값을 반환
union : 두 도시를 연결하여 parents값을 동일하게 만들어준다.
'''
input = open(0).readline
 
def solution():
    def find(a): # parents 찾기
        if a != parents[a] : # a가 a와 연결된 도시 중 최소값이 아니면
            parents[a] = find(parents[a]) # 최소값 찾을 때까지 재귀함수 반복
        return parents[a] # 찾은 parents를 반환
    
    def union(a,b): # 두 도시 연결
        a,b = find(a), find(b) # a,b는 각 도시와 연결된 최소 번호의 도시로 초기화
        if a < b : # a가 더 작으면
            parents[b] = a
        else : # b가 더 작으면
            parents[a] = b
    
    n = int(input()) # 도시의 수
    m = int(input()) # 여행계획에 포함된 도시 수
    parents = list(range(n+1)) # parents[a] = a 도시와 연결된 가장 작은 도시 번호
    for i in range(n): # 도시번호는 i+1
        connect = list(map(int,input().split()))
        for j in range(i+1,n):
            if connect[j] : # 1로 연결되어있다면
                union(i+1,j+1) # 두 도시 연결
    plan = list(map(int,input().split())) # 여행 계획에 속한 도시
    sta_city = find(plan[0]) # 여행 첫 도시
    for i in range(1,m) :
        if find(plan[i]) != sta_city : # 해당 도시의 parents와 여행 첫 도시가 다르면
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    print(solution())