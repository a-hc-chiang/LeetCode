class Solution:
    def getLucky(self, s: str, k: int) -> int:
        '''
        My Solution's Complexity
        Runtime: o(n^2) 
        Memory Usage: o(n)
        '''
        res = 0
        resStr = ""
        for c in s: 
            resStr = str((ord(c) - 96)) + resStr #taking each character's ascii values to integers 
        for i in range(k):
            res = 0 #reseting the result for each iteration of k 
            for c in resStr: 
                res += ord(c) - 48  
            resStr = str(res)
        return res
