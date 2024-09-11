class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startBinary = self.toBinary(start)
        goalBinary = self.toBinary(goal)
        res = 0 

        if len(startBinary) < len(goalBinary): #if lengths of strings don't match
            diff = len(goalBinary) - len(startBinary)
            for i in range(diff): 
                startBinary = "0" + startBinary
        elif len(startBinary) > len(goalBinary): 
            diff = len(startBinary) - len(goalBinary)
            for i in range(diff): 
                goalBinary = "0" + goalBinary

        for i in range(len(startBinary)): # only need to count if bits don't match
            if startBinary[i] != goalBinary[i]:
                res += 1
        return res

    def toBinary(self, num): 
        binaryRep = ""
        while num > 0: #convert to binary with modulo 
            if num % 2 == 1: 
                binaryRep = "1" + binaryRep 
            else: 
                binaryRep = "0" + binaryRep
            num = floor(num/2)
        return binaryRep