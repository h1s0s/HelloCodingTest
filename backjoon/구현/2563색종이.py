if __name__ == "__main__":
    paper = [[0] * 101 for i in range(101)] # 100x100 2차원 배열 생성

    for _ in range(int(input())):
        a, b = map(int, input().split())
        for i in range(10): #10X10의 정사각형을 그림
            for j in range(10):
                paper[a + i][b + j] = 1

    r = 0
    for i in paper:
        r += sum(i)
    print(r)