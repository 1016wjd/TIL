import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    strings = input()
    # print(strings)
    
    # char = []
    # for string in strings:
    #     char.append(string)
    #     if
        
    stack = []
    for i in range(len(strings)):
        # 차례로 stack에 담기
        stack.append(strings[i])
        # 문자가 존재하는 경우(0이 아닌 숫자이면 true) and 연속된 두 수가 같은경우
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    result = len(stack)
    
    print(f'#{tc} {result}')
            

