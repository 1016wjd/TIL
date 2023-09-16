## 1차원은 추출되어 2차원 리스트 형식으로 시도해봄 
## 'int' object is not subscriptable 에러가 나는데 왜그런지 모르겠음 .. 

import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : 화덕에 넣을 수 있는 피자의 개수
    # M : 피자의 개수 
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    pizza_idx = [i for i in range(M)]

    pizza_tuple = [[pizza[i],pizza_idx[i]] for i in range(M)]
    
    # print(pizza_tuple[0][0])

    # 화덕 
    stack = []
    

    # 화덕에 N개의 피자 넣기 치즈가 0이되면 빼고 다음피자 넣기 

    for i in range(N):
        new = pizza_tuple.pop(0)
        stack.append(new)
    # print(stack)

    # now = stack.pop(0)
    # print(now)
    # now_pizza = now[0]//2
    # print(now_pizza)
    # now[0] = now_pizza
    # print(now)

    while pizza: # 피자가 없어질 때 까지 반복문 돌리기!!
        # 화덕 돌리면서 1바퀴 돌리면 치즈 c//2 되도록하기 
        now = stack.pop(0)
        now_pizza = now[0]//2
        now[0] = now_pizza
        if now_pizza == 0:
            new = pizza.pop(0)
            stack.append(new)
        else:
            stack.append(now)

    print(stack)


    # # 피자가 모두 둘어간 후 

    

     


