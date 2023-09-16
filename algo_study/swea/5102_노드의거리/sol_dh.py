import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def dfs(graph, start, end):
    stack = graph[start]
    visited = [0] * (V + 1)
    route = [0]*(V+1)

    while stack:
        now = stack.pop()

        if now == end:
            return route[now] + 1

        if not visited[now]:
            visited[now] = True
            stack.extend(graph[now])


        for i in graph[now]:
            if not visited[i]:
                # if not route[i]:
                route[i] = route[now] + 1


        print("visited:", visited)
        print("route:", route)

        if tc==1:
            print('visited:', visited)
            print('route:', route)
    return 0



for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    lst = [[] for _ in range(V+1)]

    for i in range(E):
        s, d = list(map(int, input().split()))

        lst[s].append(d)
        lst[d].append(s)

    S, D = list(map(int, input().split()))

    now = S

    result = dfs(lst, S, D)

    print("#{} {}".format(tc, result))
