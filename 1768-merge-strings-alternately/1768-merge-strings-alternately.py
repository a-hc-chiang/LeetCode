class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        curr = 0
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i] 
            curr = i 
        
        curr += 1 

        while curr < max(len(word1), len(word2)): 
            if curr >= len(word1): 
                res += word2[curr]
            else: 
                res += word1[curr]
            curr += 1

        return res
        