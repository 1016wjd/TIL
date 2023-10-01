import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    tree = [0]
    tree.append(numbers.pop(0))
    tree.append(numbers.pop(0))

    # print(tree.pop())      
    i = 1

    while numbers:    

        i+=1 
        child = tree[i]
        parent = tree[i//2]

        if child < parent:
            tree[i] = parent
            tree[i//2] = child
            tree.append(numbers.pop(0))           
        else: 
            tree.append(numbers.pop(0))
            
    # print(tree, i)

    parents = []

    a = N
    while a > 0:    
        a = a//2
        parents.append(tree[a])



    print(sum(parents))
                
    # 마지막 문제 답이 다름 

    # print(tree, i) # i가 N-1까지만 도는거 발견! ㅋㅎㅋㅎ