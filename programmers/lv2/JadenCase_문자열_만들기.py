def solution(s):
    array = s.split("") #s.split()은 공백을 기준으로 문자만 자르지만, s.split("")으로 사용하면 추가적인 공백이 있는 경우를 체크
    print(array)
    for i in range(len(array)):
        if type(array[i]) is str:
            array[i] = array[i].capitalize()
    return ' '.join(array)


if __name__ == "__main__":
    #18점
    print(solution("3people unFollowed me")) #"3people Unfollowed Me"
    print(solution("for the last week")) #"For The Last Week"


def solution2(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])