input = open(0).readline

def solution(n,xs):
    # 해당 좌표보다 값이 작은 중복되지 않는 원소의 개수를 뽑아야한다.
    # 중복을 제거한 좌표 배열을 오름차순한다면 좌표의 인덱스가 압축 결과가 될 것이다.
    # 좌표의 원래 순서대로 출력되어야하므로 좌표:인덱스 의 딕셔너리로 만들어서 좌표 순서대로 출력하자.
    
    # 1. 중복을 제거한 좌표 배열 오름차순 만들기
    sorted_xs = sorted(list(set(xs)))
    # 2. 중복 제거 오름차순 배열을 통해 좌표:인덱스 추가
    dic = {num:i for i,num in enumerate(sorted_xs)}
    # 3. 좌표 순서대로 ans 배열 만들기
    ans = [dic[i] for i in xs]
    return ans

if __name__ == '__main__':
    n = int(input())
    xs = list(map(int,input().split()))
    print(*solution(n,xs))