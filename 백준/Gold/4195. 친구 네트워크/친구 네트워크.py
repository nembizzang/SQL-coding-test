'''
union-find 유형의 문제에서 parents는 list 형태로 만들었으나,
이번에는 입력값이 문자열이므로 숫자로 mapping 가능한 dictionary를 만든다.
union과 find 함수를 만들어 매번 친구관계를 입력받을 때마다 매핑 후 union을 해주고,
union 진행 후 Counter 객체로 친구 네트워크 수를 출력
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
                parents[name] = name # 처음
                f_cnt[name] = 1 # 연결된 친구는 자기 자신 뿐
        union(a_name,b_name)

if __name__ == '__main__': 
    for _ in range(int((input()))) : # 테스트 케이스 수 대로 진행
        solution()