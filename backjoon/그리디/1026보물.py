if __name__ == "__main__":
    N = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse=True)
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    print(sum)

