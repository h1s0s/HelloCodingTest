def solution(number):
    answer = 0
    for x in range(0, len(number)):
        for y in range(x+1, len(number)):
            for z in range(y+1, len(number)):
                if (number[x] + number[y] + number[z]) == 0:
                    answer += 1
    return answer

if __name__ == "__main__":
    #11,663명/71%/3점
    print(solution([-2, 3, 0, 2, -5]))  # 2
    print(solution([-3, -2, -1, 0, 1, 2, 3]))  # 5
    print(solution([-1, 1, -1, 1]))  # 0

def 다른풀이1(number):
    from itertools import combinations
    cnt = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            cnt += 1
    return cnt