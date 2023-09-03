import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    color_list = []
    for i in range(N):
        a = list(map(int, input().split()))
        color_list.append(a)

    # print(N, color_list, color_list[0][0])
    # 영역 저장 
    red = []
    blue = []
    for i in range(N):
        r1 = color_list[i][0]
        c1 = color_list[i][1]
        r2 = color_list[i][2]
        c2 = color_list[i][3]
        # print(r1,r2,c1,c2)


        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                v = r*10+c 
                # print(v)
                if color_list[i][4] == 1:
                    red.append(v)
                else:
                    blue.append(v)
                

    # print(red)       
    # print(blue)
    count = 0
    for i in red:
        if i in blue:
            count += 1 


    print(f'#{tc} {count}')

