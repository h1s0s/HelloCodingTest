def twoSum1(nums, target):
    #반복문을 사용한 방법
    n = len(nums)  # nums.length
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

def twoSum2(nums, target):
    #정렬&투포인터를 사용한 방법
    n = len(nums)
    nums.sort() #시간복잡도 O(n log n) 일단 정렬
    for left in range(0, n):
        for right in range (n-1):
            return True
    return False

if __name__ == "__main__":
    print(twoSum1(nums=[4, 1, 9, 7, 5, 3, 16], target=14))