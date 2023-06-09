def solution(data):
    data = list(map(int, data.split(" ")))
    data.sort()

    result = 0 #총 그룹 수
    count = 0 #현재 그룹에 포함된 모험가 수

    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0

    return result

if __name__ == "__main__":
    print(solution("2 3 1 2 2")) #2
    #복습.
