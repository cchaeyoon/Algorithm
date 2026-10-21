from itertools import combinations

def solution(numbers):
    answer = []
    
    # 조합
    for i in combinations(numbers, 2):
        answer.append(sum(i))
        
    answer = sorted(set(answer))
    return answer