class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk) #reduces number of loops
        res = 0 #starting index 
        while k >= chalk[res]: 
            k -= chalk[res]
            res += 1
            if res == len(chalk): #reseting index 
                res = 0
        return res