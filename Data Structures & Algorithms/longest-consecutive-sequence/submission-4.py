class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)>0:
            numSet = set(nums)
            longest = 1
        else:
            longest = 0
            return longest
            

        for num in numSet:
            if num-1 in numSet: # if not the start of a sequence
                continue
            elif num+1 in numSet: # if there are numbers after it
                currLen = 1
                while num+1 in numSet:
                    num = num+1
                    currLen += 1
                if currLen > longest: longest = currLen
            
        return longest