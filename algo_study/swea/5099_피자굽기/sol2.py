
#튜플 형식으로 만들지 않고 인덱스와 피자를 따로 만들기!! 
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
    pizza_idx = [(i+1) for i in range(M)]


    # 화덕 
    stack = []
    stack_idx =[]
    

    # 화덕에 N개의 피자 넣기 치즈가 0이되면 빼고 다음피자 넣기 (1단계)

    for i in range(N):
        new = pizza.pop(0)
        stack.append(new)

        new_idx = pizza_idx.pop(0)
        stack_idx.append(new_idx)
    # print(stack, stack_idx)

    # now = stack.pop(0)
    # print(now)
    # now_pizza = now[0]//2
    # print(now_pizza)
    # now[0] = now_pizza
    # print(now)

    # 피자가 없어질 때 까지 반복문 돌리기!! (2단계)
    while pizza: 
        # 화덕 돌리면서 1바퀴 돌리면 치즈 c//2 되도록하기 
        now = stack.pop(0)//2
        now_idx = stack_idx.pop(0)
        if now == 0:
            new = pizza.pop(0)
            new_idx = pizza_idx.pop(0)
            stack.append(new)
            stack_idx.append(new_idx)
        else:
            stack.append(now)
            stack_idx.append(now_idx)
    # print(stack, stack_idx)


    ## 피자가 모두 둘어간 후 (3단계)
    while len(stack) > 1:
        now = stack.pop(0)//2
        now_idx = stack_idx.pop(0)
        if now != 0:
            stack.append(now)
            stack_idx.append(now_idx)
        
    # print(stack, stack_idx)


    print(f'#{tc} {stack_idx[0]}')

     

## 고민해봐야할 내용 
## 더 3가지 단계를 한번에 할 수 없을까?

