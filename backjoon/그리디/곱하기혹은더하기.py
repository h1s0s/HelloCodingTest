def solution(s):
    answer = 0
    array = list(map(int, s))
    for i in range(1, len(array)):
        if i == 1:
            if array[i-1] == 0:
                answer += array[i]
            else:
                answer = array[i-1]
                answer *= array[i]
        else :
            answer *= array[i]
    return answer

if __name__ == "__main__":
    print(solution("02984"))
    print(solution("567"))
