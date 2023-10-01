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

    child = tree[N]
    parent = tree[N//2]

    if child < parent:
        tree[N] = parent
        tree[N//2] = child          

    parents = []

    a = N
    while a > 0:    
        a = a//2
        parents.append(tree[a])



    print(f'#{tc} {sum(parents)}')
