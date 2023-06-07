def solution(n, count=0):
    array = [500, 100, 50, 10]
    for coin in array:
        count += n//coin
        n %= coin
    return count

if __name__ == "__main__":
    print(solution(1260)) #시간복잡도 O(K) k는 화폐 가짓수
