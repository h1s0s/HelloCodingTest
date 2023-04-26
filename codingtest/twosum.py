def twoSum(nums, target):
    n = len(nums)  # nums.length
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

if __name__ == "__main__":
    print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))