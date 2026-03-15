def solution(s):
    answer = True
    
    arr = []
    for i in s:
        if i == '(':
            arr.append(i)
        elif i == ')':
            if len(arr) == 0:
                arr.append(i)
            else:
                arr.pop()
        
    if len(arr) != 0:
        answer = False
    elif len(arr) == 0:
        answer = True

    return answer