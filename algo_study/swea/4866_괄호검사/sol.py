import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    strings = input()
    # print(strings)
    # print(a[0])

    pl = ['(', ')', '{', '}']
    pls = []
    for i in range(len(strings)):
        if strings[i] in pl: 
            a = strings[i]
            pls.append(a)
    # print(pls)
    
    stack = [ ]

    for i in range(len(pls)):
        # print(stack)
        if pls[i] == '(' or pls[i] == '{':
            stack.append(pls[i])
        else:
            if len(stack) == 0:
                stack.append(pls[i])
            elif pls[i] == ')' and stack[-1] == '(':
                stack.pop() 
            elif pls[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                break

    if len(stack):
        result = 0
    else:
        result = 1

                
    print(f'#{tc} {result}')

    # 강사님 풀이
    # for char in pls:
    #     if char == '(' or char == '{':
    #         stack.append(char)
    #     elif len(stack) and char == ')' and stack[-1] == '(':
    #         stack.pop()
    #     elif len(stack) and char == '}' and stack[-1] == '{':
    #         stack.pop()
    #     else:
    #         stack.append(char)

    # # print(stack)

    # if len(stack):
    #     result = 0
    # else:
    #     result = 1 
    

    # print(f'#{tc} {result}')






