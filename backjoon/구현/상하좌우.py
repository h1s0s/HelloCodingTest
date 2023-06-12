def solution(n, x):
    for i in range(n):
        for j in range(x):
            print('(', i, ', ', j, ')', end=' ')
        print()

if __name__ == "__main__":
    print(solution(4, 4))