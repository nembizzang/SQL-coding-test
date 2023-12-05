'''
전위 순회 결과는 루트/왼쪽/오른쪽 이다. 그리고 왼쪽은 루트보다 작고 오른쪽은 루트보다 크다.
입력값이 50 30 24 5 28 45 98 52 60 일때
루트/왼쪽/오른쪽 : 50 / 30 24 5 28 45 / 98 52 60 이다.
이를 재귀함수를 통해 마지막 노드에 다다를때까지 루트/왼쪽/오른쪽의 구조를 찾아서
마지막 노드부터 후위 순회 결과 왼쪽/오른쪽/루트로 출력하자.
'''
import sys
sys.setrecursionlimit(10 ** 9)
input = open(0).readline # 모든 줄을 한 번에 받을 것이기에 readlines

def solution():
    tree = []
    while True:
        try:
            tree.append(int(input()))
        except:
            break

    def postord(root_idx,end_idx) :
        if root_idx > end_idx : # 노드가 50, 30처럼 루트/왼쪽 노드 만 있을 경우 대비
            return
        root = tree[root_idx]
        right_idx = root_idx+1 # 오른쪽 노드 시작은 루트 노드 다음 인덱스부터 가능
        for i in range(right_idx, end_idx+1) :
            if tree[i] > root : # 오른쪽 노드의 시작은 루트보다 처음으로 큰 수
                right_idx = i
                break
        postord(root_idx+1, right_idx-1) # 왼쪽 노드 재귀 진행
        postord(right_idx,end_idx) # 오른쪽 노드 재귀 진행
        print(root) # 루트 노드 출력
        return
    
    postord(0,len(tree)-1)
    
if __name__ == '__main__':
    solution()