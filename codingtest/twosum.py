def twoSum1(nums, target):
    #ArrayList - 반복문을 사용한 방법
    n = len(nums)  # nums.length
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

def twoSum2(nums, target):
    #ArrayList - 정렬&투포인터를 사용한 방법
    nums.sort() #시간복잡도 O(n log n) 일단 정렬
    l, r = 0, len(nums)-1
    while l<r:
        if nums[l] + nums[r] > target: #시간복잡도O(1)이 n번 반복되기에 O(n)
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True
    return False

if __name__ == "__main__":
    print(twoSum1(nums=[4, 1, 9, 7, 5, 3, 16], target=14))
    print(twoSum2(nums=[2,1,5,7], target=4))