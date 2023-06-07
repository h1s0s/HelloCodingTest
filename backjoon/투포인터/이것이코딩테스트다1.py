def solution(arr, m):
    count = end = sum = 0
    for start in range(len(arr)):
        while sum < m and end < len(arr):
            sum += arr[end]
            end += 1
        if sum == m:
            count += 1
        sum -= arr[start]
    return count

if __name__ == "__main__":
    #특정한 합을 가지는 부분 연속 수열 찾기
    #부분"연속"수열을 찾는 문제일때 사용하자
    print(solution([1,2,3,2,5],5))
