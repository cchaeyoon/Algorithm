def solution(numbers):
    answer = 0
    # not in: 리스트, 튜플, 문자열 등의 컨테이너에서 포함되어 있지 않은지 확인
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer