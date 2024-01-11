import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    numbers = [0] * (N+1)

    for i in range(M):
        idx, number = map(int, input().split())
        numbers[idx] = number

    # print(numbers)

    stack = []

    if N%2 == 0:
        numbers[N//2] = numbers[N] 

        for i in range(N-1,1,-1):
            stack.append(numbers[i])

            if len(stack) == 2:
                numbers[i//2] = sum(stack)
                stack.pop()
                stack.pop()
    else:
        for i in range(N,1,-1):
            stack.append(numbers[i])

            if len(stack) == 2:
                numbers[i//2] = sum(stack)
                stack.pop()
                stack.pop()

    # print(numbers)

    print(f'#{tc} {numbers[L]}')
    