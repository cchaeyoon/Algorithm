def solution(id_pw, db):
    answer = ''
    wrongpw = 0
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:
            answer = 'login'
            continue
        elif i[0] == id_pw[0] and i[1] != id_pw[1]:
            wrongpw += 1
            continue
        else:
            continue
    if wrongpw == 1:
        answer = 'wrong pw'
    elif wrongpw == 0 and answer != 'login':
        answer = 'fail'
    return answer