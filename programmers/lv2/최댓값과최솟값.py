def solution(s):
    array = s.split(" ")
    max = min = array[0]
    for i in range(0, len(array)):
        if int(array[i]) >= int(max):
            max = array[i]
        if int(array[i]) <= int(min):
            min = array[i]
    return min + " " + max


if __name__ == "__main__":
    #31,167명/79%/5점
    print(solution("1 2 3 4")) #"1 4"
    print(solution("-1 -2 -3 -4")) #"-4 -1"
    print(solution("-1 -1")) #"-1 -1"

def 다른풀이1(s):
    #내장 함수를 이용한 풀이
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))