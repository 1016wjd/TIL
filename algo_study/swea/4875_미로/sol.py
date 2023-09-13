import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

# def dfs():


T = int(input())

for tc in range(1, T+1):
    
    N = int(input())
    
    # 띄어쓰기 없으므로 split 안해도 됨
    miro = [list(map(int, input())) for _ in range(N)]
    
    # pprint(miro) 
    
    #시작점찾기
    for i in range(N): 
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)
    # print(start)

    stack = []
    stack.append(start)
    # print(stack)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    result = 0

    while len(stack):

        now = stack.pop()
        x, y = now[0], now[1]
        
        ## 방문한 곳은 기록! 
        miro[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 가장자리인 경우 제외
            if 0  <= nx < N and 0 <= ny < N:

                if miro[nx][ny] == 0:
                    stack.append((nx, ny))
                elif miro[nx][ny] == 3:
                    result = 1 
                    break
                # else:
                #     pass

    print(f'#{tc} {result}')


        
