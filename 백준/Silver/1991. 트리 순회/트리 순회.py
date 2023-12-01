'''
각 탐색 방법에 따라 방문하는 노드 순서를 출력해야한다.
각 방식 별로 루트, 왼쪽 자식, 오른쪽 자식의 순서를 다르게 출력하게 되므로
A를 루트 노드로 하는 클래스 객체를 만들고 각 방식별 재귀함수 메소드를 만들자
모든 탐색 결과를 포함하여 반환하는 정답 출력 메소드를 만들어 한번에 정답을 얻어내자.
'''
from collections import defaultdict
input = open(0).readline

def solution():
    n = int(input()) # 노드 개수
    tree = defaultdict(list) # 노드별 왼쪽, 오른쪽 자식
    for _ in range(n):
        p,l,r = input().split()
        tree[p]=[l,r]
    # 탐색 방식별 클래스 생성
    class travel() : # 탐색 객체 생성
        def __init__(self,root): # 생성자로 속성 생성
            self.ans = ['','',''] # 전위, 중위, 후위 결과값 담아주는 속성
            self.root = root # root 속성 생성
        
        def make_output(self) :
            self.preord(self.root)
            self.inord(self.root)
            self.postord(self.root)
            for res in self.ans :
                print(res)
        
        def preord(self,node): # 루트/왼쪽/오른쪽
            left,right = tree[node]
            self.ans[0] += node # 루트 입력
            if left != '.' : # 왼쪽 자식이 있다면
                self.preord(left)
            if right != '.' : # 오른쪽 자식이 있다면
                self.preord(right)
                
        def inord(self,node): # 왼쪽/루트/오른쪽
            left,right = tree[node]
            if left != '.' : # 왼쪽 자식이 있다면
                self.inord(left)
            self.ans[1] += node # 루트 입력
            if right != '.' : # 오른쪽 자식이 있다면
                self.inord(right)
            
        def postord(self,node): # 왼쪽/오른쪽/루트
            left,right = tree[node]
            if left != '.' : # 왼쪽 자식이 있다면
                self.postord(left)
            if right != '.' : # 오른쪽 자식이 있다면
                self.postord(right)
            self.ans[2] += node # 루트 입력

    search = travel('A') # A를 루트 노드로 하는 travel 인스턴스 생성
    search.make_output()

if __name__ == '__main__':
    solution()