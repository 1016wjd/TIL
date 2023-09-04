import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # print(str1, str2)

    N = len(str1)
    M = len(str2)

    result = 0
    for i in range(M-N+1):
        # print(tc ,str2[i:i+N])
        if str2[i:i+N] == str1:
            result = 1
            break
        else:
            result = 0
        
    print(f'#{tc} {result}')