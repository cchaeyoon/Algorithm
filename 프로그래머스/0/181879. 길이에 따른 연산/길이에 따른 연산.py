import math

def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        # 리스트의 모든 원소 곱하기
        answer = math.prod(num_list)
    return answer