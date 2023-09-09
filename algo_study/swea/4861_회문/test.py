import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    l = []
    for i in range(N):
        string = input()
        l.append(string)

    # print(l)

    # 가로 회문 탐색
    for i in range(N):
        # 반복횟수 세어주기 위한 변수 초기화
        count = 0
        for j in range(M // 2):
            if l[i][j] == l[i][M - 1 - j]:
                count += 1
                if count == (M // 2) :
                    for a in range(N-M+1):        
                        result = l[i][a:a+M+1]
                        print(f'#{tc} {result}')

    for i in range(N):
        count = 0
        for j in range(M // 2):
            if l[j][i] == l[M - 1 - j][i]:
                count += 1
                if count == (M // 2) :
                    for a in range(N-M+1):        
                        result = l[a:a+M+1][i]
                        print(f'#{tc} {result}')


# 세로 회문 탐색
    # for i in range(N):
    #     # 반복횟수 세어주기 위한 변수 초기화
    #     count = 0
    #     for j in range(M // 2):
    #         if l[j][i] == l[M - 1 + j][i]:
    #             count += 1
    #             # 조건을 만족하여 count가 M//2와 같아지면
    #             # 입력 받은 리스트의 문자열을 출력
    #             if count == (M // 2) :
    #                 for k in range(M):
    #                     result += l[k][i]
    #         else:
    #             break