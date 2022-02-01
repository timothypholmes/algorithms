
nums = [2, 7, 11, 15]
target = 9

visited_set = set()


def getSum(nums, target):
    for num in nums:
    
        if target_num in visited_set:
            return [num, target_num]
        else:
            visited_set.add(num)
    return [-1]


if __name__ == "__main__":
    [num, target_num] = getSum(nums, target)
    print('num: {}\ntarget: {}'.format(num, target))
