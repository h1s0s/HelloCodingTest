def solution(s):
    array = list(map(int, s))
    array = [item for item in array if item != 0] #리스트 컴프리헨션으로 0 빼는 로직 추가함
    answer = array[0]
    for i in range(1, len(array)):
        if array[i] <= 1:
            answer += array[i]
        else:
            answer *= array[i]
    return answer

if __name__ == "__main__":
    print(solution("02984"))
    print(solution("567"))
