class Solution:
    def minimumLength(self, s: str) -> int:
        # runtime complexity: o(n), space complexity: o(n) -- solution can be better by using counters tho 
        res = 0 
        curr_counter = 0
        s_dict = {} 

        for c in s: 
            res += 1 
            if c not in s_dict: 
                s_dict[c] = 1 
            else: 
                s_dict[c] += 1 
                if s_dict[c] == 3: 
                    s_dict[c] = 1
                    res -= 2 
        return res 
