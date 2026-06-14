def solution(n, words):
    answer = []
    fail = 0  # 성공 여부

    for i in range(1, len(words)):
        # 마지막이랑 첫번째 알파벳이 다른 경우 break
        if words[i][0:1] != words[i-1][-1:-2:-1]:
            fail = 1
            break
        # 이미 말한 단어와 같은 경우
        for j in words[0:i]:
            if words[i] == j:
                fail = 1
                break
            else:
                continue  
        if fail == 1:
            break
            
    if fail == 1:
        answer.append((i % n) + 1)
        answer.append((i // n) + 1)
    else:
        answer.append(0)
        answer.append(0)
    
    return answer