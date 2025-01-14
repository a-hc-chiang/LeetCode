class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # time complexity: o(n), space complexity: o(n) 
        a_set = set()
        b_set = set() 
        res = [] 
        for i in range(len(A)): 
            if A[i] not in a_set: 
                a_set.add(A[i])
            if B[i] not in b_set: 
                b_set.add(B[i])
            res.append(len(a_set.intersection(b_set)))
        return res 
