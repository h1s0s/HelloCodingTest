if __name__ == "__main__":
    array = input().split("-")
    nums = list()
    for i in array:
        nums.append(eval(i) if i.find("+") >= 0 else int(i))
    sum = nums[0]
    for i in range(1, len(nums)):
        sum -= nums[i]
    print(sum)