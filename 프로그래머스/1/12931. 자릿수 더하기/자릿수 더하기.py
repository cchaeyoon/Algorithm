def solution(n):
    answer = 0
    answer_list = list(map(int, str(n)))
    for i in answer_list:
        answer += i
    return answer