import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def dfs(graph, start, end):
    stack = graph[start]
    visited = [False] * (V + 1)

    # 스택이 빌 때까지 반복!
    # 스택이 있는 동안은 계속 돌려!
    while stack:
        now = stack.pop()

        if now == end:
            return True

        if not visited[now]:
            visited[now] = True
            stack.extend(graph[now])

    return False

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    lst = [[] for _ in range(V+1)]

    for i in range(E):
        s, d = list(map(int, input().split()))

        lst[s].append(d)

    S, E = list(map(int, input().split()))

    now = S

    print(lst)

    # visited = [False * (V+1)]

    result = 1 if dfs(lst, S, E) else 0

    print("#{} {}".format(tc, result))