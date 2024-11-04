class Solution:
    def compressedString(self, word: str) -> str:
        currChar = word[0]
        currInt = 1
        flag = True
        res = ""

        for ch in word: 
            if flag: 
                flag = False
                continue
            if currChar != ch: 
                if currInt == 0: 
                    currInt = 1
                res += str(currInt) + currChar
                currChar = ch 
                currInt = 1 
            else: 
                if currInt == 9: 
                    res += str(currInt) + currChar
                    currInt = 1 
                else: 
                    currInt += 1 
        return res + str(currInt) + word[-1]
        