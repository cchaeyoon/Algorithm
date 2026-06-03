def solution(n):
    answer = 0
    for i in range(2, n+1): # 2부터 n까지
        if i % 2 == 0:
            answer += i
    return answer