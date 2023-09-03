import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # P : 전체쪽수
    # A, B : A,B가 찾을 쪽번호
    P, A, B = map(int, input().split())
    # print(P, A, B)


    left = 1 
    right = P


    count_a = 0 
    while True:
        C = int((left+right)/2)
        # print(C)
        
        if C < A:
            left = C 
        elif C > A:
            right = C 
        else:
            break
        count_a += 1 


    left = 1 
    right = P
    count_b = 0 
    while True:
        C = int((left+right)/2)
        
        if C < B:
            left = C
            
        elif C > B:
            right = C   
        else:
            break
        count_b += 1 

    if count_a > count_b:
        result = 'B'
    elif count_a < count_b:
        result = 'A'
    else:
        result = 0

    # print(count_a, count_b)
    print(f'#{tc} {result}')

