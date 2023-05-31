def solution(t, p):
    answer = 0
    for i in range(0, len(t) + 1 - len(p)):
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1
    return answer
#str[자릿수:자릿수]를 활용한 문제

if __name__ == "__main__":
    #10,834명/70%/14점
    print(solution("3141592", "271"))  # 2
    print(solution("500220839878", "7"))  # 8
    print(solution("10203", "15"))  # 3
