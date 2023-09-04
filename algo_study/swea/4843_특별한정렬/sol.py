import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    # print(N, numbers)


    temp = []
    
    for i in range(5):
        temp.append(numbers[(N-i-1)])
        temp.append(numbers[i])

    # print(f"#{tc}", end=' ')
    # print(*temp)
    

    a = str(temp)
    print(''.join(a))




    # for i in range(5):
    #     temp.append(str(numbers[(N-i-1)]))
    #     temp.append(str(numbers[i]))


    # a = ' '.join(temp) # 문자형변수로! 
    # print(a)
