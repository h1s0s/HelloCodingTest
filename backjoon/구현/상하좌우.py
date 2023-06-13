def solution(n, plans):
    x, y = 1, 1

    #L(서), R(동), U(북), D(남) x가 행, y가 열
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        #공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        #이동
        x, y = nx, ny

    return x, y

if __name__ == "__main__":
    print(solution(5, "R R R U D D".split()))