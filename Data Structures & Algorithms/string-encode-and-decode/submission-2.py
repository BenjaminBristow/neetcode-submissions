class Solution:

    def encode(self, strs: List[str]) -> str:
        # length of legth of word, length of word number, word
        # 15Hello15World

        encoded_string = ""

        for word in strs:
            wordLen = len(word)
            numLen = len(str(wordLen))
            encoded_string += str(numLen) + str(wordLen) + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        strLen = len(s)
        index = 0

        while index <strLen:
            #getting word length
            numLen = s[index]
            index += 1
            numLen = int(numLen)

            wordLen = ""
            for i in range(numLen):
                wordLen += s[index+i]
            wordLen = int(wordLen)
            index += numLen

            word = ""
            for i in range(wordLen):
                word += s[index+i]
            index += wordLen
            
            decoded_strs.append(word)
            
        return decoded_strs
