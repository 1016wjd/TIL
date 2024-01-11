import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : 루트
    # E : 간선의 개수
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    
    arr = [[0] * (E+2) for i in range(2)]
    

    for i in range(0, E*2 , 2):
        parent = nodes[i]
        child = nodes[i+1]

        if arr[0][parent] == 0:
            arr[0][parent] = child
        else:
            arr[1][parent] = child

    # print(arr)

    stack = [N]
    count = 1 

    while stack:
        now = stack.pop()

        if arr[0][now]:
            stack.append(arr[0][now])
            count += 1
        if arr[1][now]:
            stack.append(arr[1][now])
            count += 1

    print(f'#{tc} {count}')

