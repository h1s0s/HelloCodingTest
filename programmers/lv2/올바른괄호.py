def solution2(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        if s[i] == ')':
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    #14점
    print(solution("()()"))  #True
    print(solution("(())()"))  #True
    print(solution(")()("))  #False
    print(solution("(()("))  #False
    print(solution("()())"))  #False

