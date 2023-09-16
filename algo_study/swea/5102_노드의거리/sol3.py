# max 값으로 하다보니 count와 같은 상황이 되어버림 

import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # V: 노드의 개수 E: 간선의 개수
    V, E  = map(int, input().split())
    # print(V, E)
    graph = [[0]*(V+1) for _ in range(V+1)] # 행과 열의 개수가 달랐음 

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1 
        graph[end][start] = 1
    
    S, G = map(int, input().split())

    # pprint(graph)

    # 방문 번호 기록
    visited = [0] * (V+1)

    now = S
    # 스택기록
    stack = []
    stack.append(now)
  
    # # 시작점 설정
    # visited[now] = 1
    
    result = 0
    # 스택이 빌때까지
    while stack:

        now = stack.pop()

        for i in range(1,V+1):
            if graph[now][i] == 1:
                if visited[i] == 0:
                    visited[i] == max(visited)+1
                    stack.append(i)

    # print(max(visited))

    # if visited[G] > 0:
    #     result = visited[G]
    # else:
    #     result = 0
                    
 
    result = visited[G]

    print(f'#{tc} {result}')