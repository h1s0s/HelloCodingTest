if __name__ == "__main__":
    A = list(map(int, input().split()))
    standard = (1, 1, 2, 2, 2, 8)
    list = list()
    for i in range(len(A)):
        if A[i] == standard[i]:
            list.append(0)
            continue
        list.append(standard[i] - A[i])
    for i in list:
        print(i, end=" ")