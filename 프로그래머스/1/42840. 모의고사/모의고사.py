def match_pattern(answers, pattern):
    count = 0
    for i in range(len(answers)):
        if answers[i] == pattern[i % len(pattern)]:
            count += 1
    return count

def solution(answers):
    answer = []
    
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a1 = match_pattern(answers, p1)
    a2 = match_pattern(answers, p2)
    a3 = match_pattern(answers, p3)
    
    m = max(a1, a2, a3) # 문제 맞힌 개수 중 max값 추출 2, 2, 2
    if a1 == m:
        answer.append(1)
    if a2 == m:
        answer.append(2)
    if a3 == m:
        answer.append(3)
        
    return answer