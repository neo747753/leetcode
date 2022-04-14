# -*- coding: utf-8 -*-


def twoSum1(nums, target):
    """解法1"""
    for index, value in enumerate(nums):
        if target - nums[index] in nums and index != nums.index(target - nums[index]):
            return [index, nums.index(target - nums[index])]


def twoSum2(nums, target):
    """解法2"""
    hash_map = {}
    for index, value in enumerate(nums):
        hash_map[value] = index

    for index, value in enumerate(nums):
        tmp_index = hash_map.get(target - value)
        if index != tmp_index and tmp_index is not None:
            return [index, tmp_index]


if __name__ == "__main__":
    nums = [3, 3, 4]
    target = 7
    print(twoSum1(nums, target))
    print(twoSum2(nums, target))
