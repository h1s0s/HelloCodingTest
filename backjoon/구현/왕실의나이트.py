def solution(n):
    #현재 위치
    row = int(n[1])
    column = int(ord(n[0])) - int(ord('a')) +1

    #이동할 수 있는 방향 정의
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    result = 0

    #이동이 가능한지 확인
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        #이동 가능하면 카운트 증가
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
            result += 1
    return result

if __name__ == "__main__":
    print(solution("a1"))