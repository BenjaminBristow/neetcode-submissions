class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dic = {}
        

        for word in strs:
            dic = {}
            
            for char in word:
                dic[char] = dic.get(char,0)+1

            dicset = tuple(sorted(dic.items()))
            

            answer_dic[dicset] = answer_dic.get(dicset, [])
            answer_dic[dicset].append(word)
        
        output = list(answer_dic.values())
        
        return output