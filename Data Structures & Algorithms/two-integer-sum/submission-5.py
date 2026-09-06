class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in dic:
                return [dic[difference], i]
            dic[num] = i
