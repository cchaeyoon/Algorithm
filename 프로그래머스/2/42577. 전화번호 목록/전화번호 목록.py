def solution(phone_book):
    answer = True
    
    # 문자열의 접두사 확인하기 위해서: startswith()
    # b.startswith(a) -> b가 a로 시작하는지 (a는 b의 접두사)

    # 정렬을 하면 이웃한 번호만 비교하면 됨!!
    phone_book.sort()
    
    for i in range(0, len(phone_book)): 
        if i + 1 == len(phone_book):
            break
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break

    return answer