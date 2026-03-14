def solution(participant, completion):
    p = {}
    
    for name in participant:
        p[name] = p.get(name, 0) + 1
        
    for name in completion:
        p[name] -= 1
        
    for name, count in p.items():
        if count > 0:
            answer = name
            
    return answer