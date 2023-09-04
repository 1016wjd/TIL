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
    temp = []
    
    for i in range(len(str1)):
        count = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
        # print(count)
        temp.append(count)
    result = max(temp)
    # print(temp, result)
    print(f'#{tc} {result}')
    
