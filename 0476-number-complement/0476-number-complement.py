class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        binaryRep = ""
        while num > 0: #convert to binary with modulo 
            if num % 2 == 1: 
                binaryRep = "1" + binaryRep 
            else: 
                binaryRep = "0" + binaryRep
            num = floor(num/2)
        exp = 0 
        for i in binaryRep[::-1]: #convert to decimal 
            if i == "0": # switch condition for complement 
                res += pow(2, exp)
            exp += 1
        return res