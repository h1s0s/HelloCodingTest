def solution(n, k):
    count = 0
    while True:
        target = (n // k) * k #나눌 수 있는(몫이 0인) 값을 구함
        count += (n - target) #n에서, 나눌수 있는 값까지 -1을 반복한 것이니까 빼서 카운트에 더해줌
        n = target #n의 값도 바꿔줌
        if n < k:

            break
        count += 1
        n //= k
    count += (n-1)
    return count

def solution2(n, k):
    count = 0
    while n != 1:
        if n % k == 0:
            n //= k
            count += 1
        else:
            n -= 1
            count += 1
    return count

if __name__ == "__main__":
    print(solution(25, 3))
    print(solution2(25, 3))
