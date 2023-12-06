'''
union-find 유형의 문제에서 parents는 list 형태로 만들었으나, 이번에는 입력값이 문자열이므로 dictionary 형태로 만든다.
매번 친구 관계 입력값을 받을 때마다 Union을 실행하여 한 쪽으로 parents를 맞춰주고 상위 parents인 쪽에 친구의 수를 더해준다.
* 수 형태에선 작은 값으로 부모를 맞춰주는게 시간 단축에 유리하나 안 맞춰주어도 무방하다. 어차피 find에서 부모를 끝까지 찾아간다.
'''
input = open(0).readline

def solution():
    def find(a):
        if a != parents[a]: # a가 a의 친구관계 중 최소값이 아니라면
            parents[a] = find(parents[a]) # parents의 parents 찾기
        return parents[a] # 찾은 parents를 반환
    
    def union(a,b): # 입력값은 이름이 매핑된 숫자가 들어감
        a,b = find(a),find(b) # a,b는 a,b의 친구관계 중 최소값으로 초기화
        if a != b : # parents 값이 다르다면
            parents[b] = a # parents[b]를 a로 동일하게 만들어줌
            f_cnt[a] += f_cnt[b] # a의 친구 수에 b의 친구 수를 더해줌
        print(f_cnt[a])

    f = int(input()) # 친구 관계의 수
    parents, f_cnt = {}, {} # 연결된 친구를 담는 딕셔너리, 연결된 친구의 수
    for _ in range(f) :
        a_name,b_name = input().split()
        for name in [a_name,b_name]:
            if name not in parents : # 처음 입력받는 이름이면
                parents[name] = name # 부모에 자기 자신 넣어두기
                f_cnt[name] = 1 # 연결된 친구의 수는 1(자기 자신 뿐)
        union(a_name,b_name)

if __name__ == '__main__': 
    for _ in range(int((input()))) : # 테스트 케이스 수 대로 진행
        solution()