def solution(n, h):
    h.sort()
    length = n[1]
    for l in h:
        if l <= length:
            length += 1
    return length

if __name__ == "__main__":
    # n = list(map(int, input().split()))
    # h = list(map(int, input().split()))
    # print(solution(n, h))
    print(solution([3, 10], [10, 11, 13])) #12
    print(solution([9, 1], [9, 5, 8, 1, 3, 2, 7, 6, 4])) #10