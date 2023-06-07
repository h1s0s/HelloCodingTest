def solution(n,p):
    p.sort()
    sum = i = 0
    while i <= n:
        for e in range(0, i):
            sum += p[e]
        i += 1
    return sum

if __name__ == "__main__":
    # n = int(input())
    # p = list(map(int,input().split()))
    # print(solution(n, p))
    print(solution(5, [3, 1, 4, 3, 2])) #32
