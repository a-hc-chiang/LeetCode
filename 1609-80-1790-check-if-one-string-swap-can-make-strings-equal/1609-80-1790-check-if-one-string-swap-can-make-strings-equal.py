class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {} 
        diff = 0 
        for i in range(len(s1)): 
            if s1[i] not in s1_dict:
                s1_dict[s1[i]] = 1 
            else: 
                s1_dict[s1[i]] += 1 
            if s2[i] not in s2_dict:
                s2_dict[s2[i]] = 1 
            else: 
                s2_dict[s2[i]] += 1 
            if s1[i] != s2[i]: 
                diff += 1 
        if s2_dict != s1_dict: 
            return False 
        return diff < 3