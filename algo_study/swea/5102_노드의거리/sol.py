import sys
from pathlib import Path
from pprint import pprint
file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    arr = [ ([0] * (V+1)) for _ in range(V+1)]
    # pprint(arr)

    # 시작점 설정
    for i in range(E):
        node1, node2 = map(int, input().split())
        #양방향 노드설정
        arr[node1][node2] = 1
        arr[node2][node1] = 1

    S, G = map(int, input().split())

    # print(V, E, S, G)
    # pprint(arr)



    # 방문기록
    visited = [0] * (V+1)

    # 시작점 스택에 넣기 
    now = S 
    stack = []
    stack.append(now) 
    

    while stack:
        now = stack.pop()
        # visited[now] = True 
        
        for i in range(1, V+1): # 이 코드가 현재 now와 연결된 것을 스택에 넣고 처리! 
            if arr[now][i] == 1:
                if visited[i] == 0:
                    stack.append(i)
                    visited[i] = visited[now]+1
                    # print(stack)
                    # print(visited)

    
    print(f'#{tc} {visited[G]}')