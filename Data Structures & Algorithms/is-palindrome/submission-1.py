class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        palindrome = True
        length = len(s)
        if length % 2 == 0:
            midpoint = length / 2
            x=0
            while x < midpoint:
                if s[x] == s[-x-1]:
                    x+=1
                    palindrome = True
                else:
                    palindrome = False
                    break
        else:
            midpoint = (length / 2) + 0.5
            x = 0
            while x < midpoint:
                if s[x] == s[-x-1]:
                    x+=1
                    palindrome = True
                else:
                    palindrome = False
                    break

        if palindrome == True:
            return True
        else:
            return False
