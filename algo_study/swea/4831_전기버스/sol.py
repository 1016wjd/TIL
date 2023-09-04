import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # K: 한번에 이동할 수 있는 정류장 수
    # N : 종점 , 정류장 수
    # M : 충전기가 설치된 정류장의 수 
    K, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    

    count = 0 # 최대 충전 횟수 
    now = 0 # 현재 위치 
    
    # 1. if 현재위치가 종점인 경우 break 
    # 2.  else 아닌경우 최대로 이동
    # 3. 와일 문 이용 ! 종점에 도착할 때까지 반복 
    #     > 가장 가까운 충전소로 이동! 
    #     > 충전하고 카운트 증가 

    # 현재위치가 종점에 도착한 경우
    # if now >= N:
         
    # 아직 도착하지 않은경우 
    # else:
        # 종점에 도착할 때 까지 가장 가까운 충전소로 이동! 
    while now+K < N:

        for i in range(now+K, now, -1):
            
            if i in numbers:
                now = i
                count += 1
                # print(now, count) 
                break
        # for 문에 대한 else는 중간에 빠져나오지 않고  끝까지 실행 죈 경우 else문이 실행 
        else:
            count = 0
            now = N

    print(f'#{tc} {count}')
                    
            


#    set을 이용한 풀이
#    nums = list(map(int, input().split()))

#     answer = 0

#     now = 0
#     while now<N-K:
#         if len(set(nums) & set(range(now+1, now+K+1))):
#             now = max(set(nums) & set(range(now+1, now+K+1)))
#             answer += 1

#         else:
#             answer = 0
#             break



#     print("#{} {}".format(tc, answer))       