import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    char = []
    for i in range(N):
        string = input()
        char.append(string)
    # print(N, M ,char)
    
    char_t = list(map(list,zip(*char)))
    # print(char_t)

  
     
    # for i in range(N):
    #     # 행
    #     if char[i] ==char[i][::-1]:
    #         result = char[i]
    #         break      
    #         # 열
    #     if char_t[i] ==char_t[i][::-1]:
    #         result_1 = char_t[i]
    #         result = ''.join(result_1)
    #         break  
        
        
    for i in range(N):
        for j in range(N-M+1):
            # 행
            if char[i][j:j+M] ==char[i][j:j+M][::-1]:
                result = char[i][j:j+M]
                break      
                # 열
            if char_t[i][j:j+M] ==char_t[i][j:j+M][::-1]:
                result_1 = char_t[i][j:j+M]
                result = ''.join(result_1)
                break  
            

    print(f'#{tc} {result}')


    