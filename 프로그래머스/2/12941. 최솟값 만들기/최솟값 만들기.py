def solution(A,B):
    answer = 0
    
    # 한 배열의 가장 작은 값 * 다른 배열의 가장 큰 값
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer