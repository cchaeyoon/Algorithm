def solution(s):
    mid = (len(s) + 1 ) // 2 
    if len(s) % 2 == 0: # 짝수인 경우
        answer = s[mid-1] + s[mid]
    else:
        answer = s[mid-1]
    return answer