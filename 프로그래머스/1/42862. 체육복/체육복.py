def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)  # 원래 체육복 가져온 수
    
    # 여벌 가져온 애 중 잃어버린 애를 처리해야함
    common = set(lost) & set(reserve) # 교집합
    answer += len(common)
    lost = [x for x in lost if x not in common]
    reserve = [x for x in reserve if x not in common]
    
    lost.sort()
    reserve.sort()
    
    for i in lost:
        for j in reserve:
            if (i - 1 == j or i + 1 == j):
                answer += 1
                reserve.remove(j)
                break
        
    return answer