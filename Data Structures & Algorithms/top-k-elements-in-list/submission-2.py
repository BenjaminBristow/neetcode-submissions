class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        numCountList = sorted(numCount, key=numCount.get, reverse=True)

        result = []
        for i in range(k):
            result.append(numCountList[i])
        
        return result