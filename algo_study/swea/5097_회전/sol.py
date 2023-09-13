import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split())) 
    
    # print(numbers)


    for i in range(M):
        a = numbers.pop(0)
        numbers.append(a)

    print(f'#{tc} {numbers[0]}')

    # print(numbers[M%N])

    