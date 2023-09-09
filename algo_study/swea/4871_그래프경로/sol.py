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
    
    S, G = map(int, input().split())

    # pprint(graph)
  
    # 방문기록
    visited = [False] * (V+1)

    now = S
    # 스택기록
    stack = []
    stack.append(now)
  
    # 시작점 설정
    visited[now] = True 
    
    result = 0
    # 스택이 빌때까지
    while stack:

        now = stack.pop()
        visited[now] = True

        for i in range(1,V+1):
            if graph[now][i] == 1:
                if visited[i] == False:
                    visited[i] == True
                    stack.append(i)

    #이프분을 밑으로 내려야함 
    if visited[G] == True:
        result = 1
    else:
        result =0
                    
 

    print(f'#{tc} {result}')

                        


# ## 런타임에러 > 시간이 아니라 돌리는 중 (=  런타임)에 에러가 남
        

        
    

