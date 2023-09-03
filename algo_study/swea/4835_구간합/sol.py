import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : 정수의 개수
    # M : 구간의 개수
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # print(N, M, numbers)

    sum_list = [] 
    for i in range(N-M+1):
        # print(numbers[i:i+M])
        a = sum(numbers[i:i+M])
        # print(a)
        sum_list.append(a)
    # print(sum_list)

    result = max(sum_list) - min(sum_list)
    print(f'#{tc} {result}')

