import sys
from pathlib import Path
import copy
from copy import deepcopy

file_path = Path(file).parent
input_path = file_path / 'input.txt'

sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):

    phr = list(str(input()))

    phr2 =[]

    while True:


        while len(phr):
            char = phr.pop()

            if len(phr2):

                if char == phr2[-1]:
                    phr2.pop()

                else:
                    phr2.append(char)

            else:
                phr2.append(char)

        length = len(phr2)
        phr = phr2
        if len(phr2) == length:
            break

    print(phr2)

    print("#{} {}".format(tc, len(phr2)))