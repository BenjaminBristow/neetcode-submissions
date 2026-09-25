class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # make a dictionary for words for letters
        # for every word, make a dictionary of the letters and increment by one in dictionary of words if it doesnt already exist
        #loop through word dictionary printing results

        wordDic = {}

        for word in strs:
            letterDic = {}

            for letter in word:
                letterDic[letter] = letterDic.get(letter, 0) + 1
            
            key = tuple(sorted(letterDic.items()))
            wordDic[key] = wordDic.get(key, [])
            wordDic[key].append(word)
        
        return list(wordDic.values())
        