def solution():
    answer = 0
    return answer

if __name__ == "__main__":
    i = 0
    sum = 0
    while i < 10:
        i = i+1
        if i % 3 == 0:
            sum -= i
        elif i % 3 == 1:
            sum += i
        else:
            sum *= i

    print(sum)

