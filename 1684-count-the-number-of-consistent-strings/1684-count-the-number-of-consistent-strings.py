class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int: 
        allowedSet = set()
        res = 0

        for ch in allowed: 
            allowedSet.add(ch)
        
        for word in words: #brute force approach 
            i = 0 
            for ch in word: #checking each character in the word
                if ch not in allowedSet: 
                    break
                i += 1 
            if i == len(word): 
                res += 1

        return res