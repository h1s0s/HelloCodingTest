if __name__ == "__main__":
    #시뮬레이션 및 완전 탐색 문제에서는 방향 벡터가 자주 활용됨

    #동, 북, 서, 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    #현재 위치
    x, y = 2, 2

    for i in range(4):
        # 다음 위치
        nx = x + dx[i]
        ny = y + dy[i]
        print(nx, ny)