import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def inorder(idx):

    global count
    
    if idx <= N:
        
        # 왼쪽 자식
        inorder(idx*2)
        # print(tree)

        # 현재노드 
        tree[idx] = count
        count += 1 

        # 오른쪽 자식
        inorder(idx*2+1)
        # print(tree)

for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    count = 1 
     
    inorder(1)

    # print(f'#{tc} {tree[1]} {tree[N//2]}')



    

    
    