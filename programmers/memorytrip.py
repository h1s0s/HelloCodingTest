def solution(name, yearning, photo):
    answer = []
    friend = {}
    for i in range(len(yearning)):
        friend[name[i]] = yearning[i]
    for i in photo:
        result = 0
        for j in i:
            if j in friend:
                result += friend[j]
        answer.append(result)
    return answer

if __name__ == "__main__":
    name = ["may", "kein", "kain", "radi"]
    yearning = [5, 10, 1, 3]
    photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
    print(solution(name, yearning, photo))