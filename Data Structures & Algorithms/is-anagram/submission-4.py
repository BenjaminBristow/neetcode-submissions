class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        for char in s:
            dic_s[char] = dic_s.get(char, 0)+1

        dic_t = {}
        for char in t:
            dic_t[char] = dic_t.get(char, 0)+1
        
        if dic_s == dic_t:
            return True
        else:
            return False