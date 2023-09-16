import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    
    N = int(input())
    
    miro = [list(map(int, input())) for _ in range(N)]
    
    #시작점찾기
    for i in range(N): 
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)

    stack = []
    stack.append(start)

    count = [[0] * (N+1) for i in range(N+1)]
    # pprint(count)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    result = 0

    while len(stack):

        now = stack.pop()
        x, y = now[0], now[1]
        
        ## 방문한 곳은 기록! 
        # miro[x][y] = 1

        # pprint(miro)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 가장자리인 경우 제외
            if 0  <= nx < N and 0 <= ny < N:

                if miro[nx][ny] == 0:
                    stack.append((nx, ny))
                    miro[nx][ny] = 1
                    count[nx][ny] = count[x][y] + 1
                    
                elif miro[nx][ny] == 3:
                    result = count[x][y] 

                    break

            pprint(count)


    # print(f'#{tc} {result}')
