class Solution:
    def minChanges(self, s: str) -> int:
        freq = [] 
        curr = 1
        currCh = s[0]
        res = 0 
        flag = True

        for ch in s: 
            if flag: 
                flag = False
                continue 
            if ch != currCh: 
                freq.append(curr)
                curr = 1 
                currCh = ch 
            else: 
                curr += 1
        freq.append(curr)

        for i in range(len(freq)-1): 
            if freq[i] % 2 != 0: 
                freq[i] += 1
                freq[i+1] -= 1
                res += 1 
        return res

        