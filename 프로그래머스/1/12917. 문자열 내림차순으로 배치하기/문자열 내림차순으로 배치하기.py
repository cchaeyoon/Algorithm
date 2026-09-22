def solution(s):
    answer = ''
    
    # 문자열을 리스트로 변환
    arr = list(s)
    # 역순으로 정렬
    arr.sort(reverse=True)
    # 다시 문자열로 join
    answer = ''.join(arr)
    return answer