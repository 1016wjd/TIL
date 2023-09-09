import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

# 경우의 수 생각
    # a1 = 10 result = 1
    # a2 = 20 result = 3
    # a3 = 30 result = 5
    
    # a5 = a(N-2) + 2 a(N-1)

def function(n):
    if n == 1:
        return 1 
    elif n == 2:
        return 3
    else:
        return 2 * function(n-2) + function(n-1)
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = N // 10
   
    a = function(n)
    
    print(f'#{tc} {a}')
    

    

    
    
