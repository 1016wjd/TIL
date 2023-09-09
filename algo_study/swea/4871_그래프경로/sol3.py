import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def dfs(now):
    visited[now] = True

    for i in graph[now]:
        if not visited[i]:
            dfs(i)

T = int(input())

for tc in range(1, T+1):
    # V: 노드의 개수 E: 간선의 개수
    V, E  = map(int, input().split())
    # print(V, E)
    graph = [[0]*(V+1) for _ in range(V)]
    # print(graph)

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1 
    
    S, G = map(int, input().split())

    # print(V, E, graph, S, G)
  
    # 방문기록
    visited = [False] * (V+1)

    # now = S
    # 스택기록
    # stack = []
    # stack.append(now)

    dfs(S)

    print(visited)


    if 