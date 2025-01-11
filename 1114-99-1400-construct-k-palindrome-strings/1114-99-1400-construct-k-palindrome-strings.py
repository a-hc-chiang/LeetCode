class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): 
            return False
        letter_freq = {} 
        odds = 0 

        for c in s: 
            if c not in letter_freq: 
                letter_freq[c] = 1 
            else: 
                letter_freq[c] += 1 
        for ke in letter_freq: 
            if letter_freq[ke] % 2 == 1: 
                odds += 1 
        
        return odds <= k 
        
        