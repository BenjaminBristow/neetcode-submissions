class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        # prefix 
        prefix = 1
        for i in range(len(nums)):
            if i == 0:
                answer.append([1,1])
            else:
                prefix *= nums[i-1]
                answer.append([prefix,1])

        # postfix
        postfix = 1
        for i in range(len(nums)):
            if i == 0:
                answer[len(nums)-1-i][1] = postfix
            else:
                postfix *= nums[len(nums)-i]
                answer[len(nums)-1-i][1] = postfix

        # calculate        
        output = []
        for i in range(len(answer)):
            output.append(answer[i][0] * answer[i][1])

        return output

        
       