def solution(n, m, a):
    a.sort()
    l = 0
    r = n - 1
    sum = 0
    while l < r:
        if a[l] + a[r] < m: #m이 10이상일수도 있는데 이부분 생각 안했었음, 고치니까 정답
            l += 1
        else:
            sum += 1
            l += 1
            r -= 1
    return sum


if __name__ == "__main__":
    # n, m = map(int, input().split())
    # a = list(map(int,input().split()))
    # print(solution(n,m,a))
    #
    n = 6
    m = 10
    a = [3, 5, 7, 3, 5, 6]
    print(solution(n, m, a))
    n = 1
    m = 10
    a = [100]
    # n, m = map(int, input().split())
    print(solution(n,m,a))