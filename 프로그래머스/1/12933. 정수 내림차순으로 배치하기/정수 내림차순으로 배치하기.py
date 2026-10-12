def solution(n):
    answer = 0
    # 정수를 문자열로 바꾸고
    # 내림차순으로 정렬
    # ''.join으로 문자열을 결합
    num_str = int(''.join(sorted(str(n), reverse = True)))
    return num_str