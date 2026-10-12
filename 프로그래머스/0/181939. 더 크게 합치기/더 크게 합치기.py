def solution(a, b):
    answer = 0 
    # 문자열은 새 문자열을 만들어 반환하는 방식으로 처리
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    
    answer = max(int(ab), int(ba))
    return answer