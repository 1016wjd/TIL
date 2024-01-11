import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    tree = [1, 2, 4, 8, 16, 32]
    count = [sum(tree[:i]) for i in range(1,6)]
    # print(count)

    now = 0 # 가지의 층수 반환

    for i in range(5):
        if N < count[i]:
            now = i
            now_count = count[i]
            break
    # print(now, now_count)

    right_tree = (now_count - 1) / 2

    root = int(right_tree + 1)        
 
    print(root)
