'''
queue는 선입선출, 후입후출이고 / stack은 선입후출, 후입선출이다.
queue는 원래있던 숫자가 빠지고 / stack은 삽입된 숫자가 빠진다.
이를 이용해 queue일때는 원래 원소와 삽입한 원소를 바꿔주고, stack일때는 삽입한 원소를 그대로 가져가면 된다.
stack일때는 아무런 변화가 없으므로(통과!) queue 자료구조형일 때의 순서만 변경된다.
queue 자료구조형만 남겨뒀을때
맨 처음 삽입한 숫자가 제일 앞에 있고 제일 마지막의 숫자가 반환되기에
이는 queue인 자료구조형의 원소들만 모아두고 queue를 만들어서 선입선출의 구조로 만들어줘도 된다.
'''
input = open(0).readline

if __name__ == '__main__':
    n = int(input())
    list_type = list(map(int,input().split())) # 큐=0,스택=1
    list_num = list(map(int,input().split())) # 원소
    queue = [list_num[i] for i in range(n) if not list_type[i]] # 큐만 담기
    m = int(input())
    inserts = list(map(int,input().split()))
    # 현재 queue에는 맨 마지막의 원소가 맨 뒤에 있으므로
    # inserts를 포함하여 삽입순서가 오래된 순서로 정렬한다면
    queue = queue[::-1]+inserts
    # 먼저 들어간 순서로 m개만 출력이므로
    print(*queue[:m])