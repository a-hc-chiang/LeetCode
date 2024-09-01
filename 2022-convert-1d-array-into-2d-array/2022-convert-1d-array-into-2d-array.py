class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n: #if impossible to make into matrix
            return []

        res = []
        i = 0 #to keep track of the original array's index
        for j in range(0, m, 1): #matrix's row index
            res.append([]) #add new list into the matrix
            for k in range(0, n, 1): #matrix's col index
                res[j].append(original[i])
                i += 1
        return res
        