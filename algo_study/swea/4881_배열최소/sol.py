import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


# idx 행 의미 i는 열 의미 visited 열 제외  

def search(idx, visited, SUM):
    global min_sum

    if idx >= N : # 모든 행을 모두 돌때까지 
        if SUM < min_sum:
            min_sum = SUM # 최소합 갱신 
        return 

    # if SUM > min_sum:
    #     return

    for i in range(N):
        if  visited[i] == False:
            SUM += arr[idx][i]
            visited[i] = True 
            search(idx+1, visited, SUM) # 다음행에 대해 반복(재귀함수)

            # 반복문 돌리기위해 직전의 요소 다시 초기화 해주는 코드?
            SUM -= arr[idx][i]
            visited[i] = False



T = int(input())

for tc in range(1, T+1):

    N = int(input())
        
    arr = [list(map(int, input().split())) for _ in range(N)]

    # arr = [] 
    # for _ in range(N):
    #     m = list(map(int, input().split()))
    #     arr.append(m)

    # pprint(arr)


    # for i in range(N):
    #     numbers.append(arr[0][i])
    #     del arr[1][i]
    #     del arr[2][i]
    #     print(i, arr)
        # for j in range(N-1):
        #     numbers.append(arr[1][j])
        #     print(arr)
            # del arr[2][j]
            # numbers.append(arr[2][0])
            # print(sum(numbers))


    # 인덱스로 반복문을 돌리기 어려우니 visited를 통해 열체크 

    visited = [False]*N

    min_sum = 1000000000
    SUM = 0

    search(0, visited, SUM)
    print(f'#{tc} {min_sum}')



    # 질문정리 
    # Q1 : 21번째 문장은 단계를 줄이기위한 코드인건가요?
    # Q2 : 리턴은 함수를 끝내는 명령어인가요? 
    # Q3 : 글로벌변수와 매개변수?의 설정 차이를 모르겠어요 