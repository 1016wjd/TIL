import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : 원소의 개수
    # K : 원소의 합
    N , K = map(int, input().split())
    # print(N, K)
    
    numbers = list(range(1,13)) # 집합 A

    n = len(numbers) # 12
    count = 0

    # 부분집합 만들기
    for i in range(1 << n): # 2의 12승까지의 수들만큼 반복 (부분집합의 개수)
        temp = []
        for j in range(n): # 12번 반복
            if i & (1<<j): # 각 자릿수를 비교하는 조건문 0이면 F를 숫자면 T를 반환
                temp.append(numbers[j]) # 부분집합 만들기  

        # print(temp) # 모든 부분집합의 모임

        
        if len(temp) == N and sum(temp) == K:
            count += 1 
            
    print(f'#{tc} {count}')

