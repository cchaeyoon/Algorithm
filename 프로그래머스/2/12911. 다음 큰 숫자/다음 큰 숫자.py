def solution(n):
    one = bin(n)[2:].count('1')
    answer = n + 1
    while (bin(answer)[2:].count('1') != one):
        answer += 1
    return answer