def solution(t, p):
    answer = 0
    for i in range(0, len(t) + 1 - len(p)):
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution("3141592", "271")) #2
    print(solution("500220839878", "7")) #8
    print(solution("10203", "15")) #3