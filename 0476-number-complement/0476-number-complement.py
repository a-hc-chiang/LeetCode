class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        binaryRep = ""
        while num > 0: #convert to binary with modulo 
            if num % 2 == 1: 
                binaryRep += "1"
            else: 
                binaryRep += "0"
            num = floor(num/2)
        binaryRep = binaryRep[::-1] #reverse string 
        exp = 0 
        for i in binaryRep[::-1]: #convert to decimal 
            if i == "0": # switch condition for complement 
                res += pow(2, exp)
            exp += 1
        return res