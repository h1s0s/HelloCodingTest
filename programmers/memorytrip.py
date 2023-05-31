def solution(name, yearning, photo):
    answer = [] #배열
    friend = {} #딕셔너리
    for i in range(len(yearning)):
        friend[name[i]] = yearning[i]
    for i in photo:
        result = 0
        for j in i:
            if j in friend: #friend에 j key값이 있는지?
                result += friend[j]
        answer.append(result)
    return answer

if __name__ == "__main__":
    name = ["may", "kein", "kain", "radi"]
    yearning = [5, 10, 1, 3]
    photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
    print(solution(name, yearning, photo))

def 다른풀이1(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]