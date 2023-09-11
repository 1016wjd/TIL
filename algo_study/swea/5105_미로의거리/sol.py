import sys
from pathlib import Path
from pprint import pprint 

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    pprint(arr)
