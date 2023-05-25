def twoSum(nums, target):
    memo = {}
    # 딕셔너리에 nums 값을 하나하나 저장
    # 복잡도 O(n)
    for v in nums:
        memo[v] = True

    # 복잡도 O(n)
    for v in nums:
        if (target - v) in d:
            return True
    return Fasle